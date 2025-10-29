<script lang="ts">
    import {T, useThrelte} from '@threlte/core';
    import {useTexture, interactivity, SVG} from '@threlte/extras';
    import WorldMap from '$lib/assets/The_Northern_Empire.png';
    import MapPinIcon from '$lib/assets/map-pin.svg';
    import type {Marker, MarkerResponse} from "$lib/interfaces/marker";

    let {marker_data} = $props();
    let existing_markers = $state(marker_data);

    interactivity();

    let distance = $state(5);
    let dragging = $state(false);
    let posX = $state(0);
    let posY = $state(0);

    let cameraX = $state(0);
    let cameraY = $state(0);

    let markers = $state([]);

    const {renderer} = useThrelte();

    $effect(() => {
        if (renderer?.domElement) {
            renderer.domElement.style.cursor = dragging ? 'grabbing' : 'pointer';
        }
    });

    const zoom = (e) => {
        distance += e.nativeEvent.deltaY / 1000;
    };

    const handleDrag = (e) => {
        if (dragging) {
            cameraX += (posX - e.nativeEvent.clientX) / 500;
            cameraY -= (posY - e.nativeEvent.clientY) / 500;

            posX = e.nativeEvent.clientX;
            posY = e.nativeEvent.clientY;
        }
    };

    const endDrag = () => {
        dragging = false;
    };

    const handleOnDblClick = async (e) => {
        let foo = {
            posX: e.point.x,
            posY: e.point.y,
        } as Marker;
        markers.push(foo);

        const params = new URLSearchParams({
            pos_x: e.point.x,
            pos_y: e.point.y
        }).toString();

        const response = await fetch("http://localhost:5000/markers?" + params, {method: 'POST'});

        if (!response.ok) {
           console.log(response);
        }
    };

    $effect(() => {
        if (existing_markers) {
            existing_markers.markers.forEach((marker: MarkerResponse) => {
                const new_marker = {
                    id: marker.id,
                    posX: marker.pos_x,
                    posY: marker.pos_y,
                } as Marker;

                if (!markers.includes(new_marker)) {
                    markers.push(new_marker);
                }
            });
        }
    });
</script>

<T.PerspectiveCamera
    makeDefault
    position={[cameraX, cameraY, distance]}
    fov={50}
    oncreate={(ref) => {
		ref.lookAt(0, 0, 0);
	}}
/>

{#await useTexture(WorldMap) then texture}
    <T.Mesh
        onwheel={(e) => zoom(e)}
        onpointerdown={(e) => {
			dragging = true;
			posX = e.nativeEvent.clientX;
			posY = e.nativeEvent.clientY;
		}}
        onpointerup={endDrag}
        onpointerleave={endDrag}
        onpointerout={endDrag}
        onpointermove={(e) => handleDrag(e)}
        ondblclick={handleOnDblClick}
    >
        <T.BoxGeometry args={[7, 4, 0]}/>
        <T.MeshBasicMaterial map={texture}/>
    </T.Mesh>
{/await}

{#each markers as marker (marker.id)}
    <T.Mesh>
        <SVG
            src={MapPinIcon}
            scale={0.005}
            position.x={marker.posX - 0.06}
            position.y={marker.posY + 0.12}
            position.z={0.0001}
        />
    </T.Mesh>
{/each}

