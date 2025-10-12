<script lang="ts">
    import {T} from '@threlte/core';
    import {useTexture, interactivity, useCursor} from '@threlte/extras';
    import WorldMap from '$lib/assets/The_Northern_Empire.png';

    interactivity();

    let distance = $state(5);
    let dragging = $state(false);
    let posX = $state(0);
    let posY = $state(0);

    let cameraX = $state(0);
    let cameraY = $state(0);

    const zoom = (e) => {
        distance += e.nativeEvent.deltaY / 1000;
    };

    const handleDrag = (e) => {
        if (dragging) {
            cameraX += (posX - e.nativeEvent.clientX) / 1000;
            cameraY -= (posY - e.nativeEvent.clientY) / 1000;
        }
    };
</script>

<T.PerspectiveCamera
    makeDefault
    position={[cameraX, cameraY, distance]}
    fov={50}
    oncreate={(ref) => {
    ref.lookAt(0, 0, 0)
  }}
/>

{#await useTexture(WorldMap) then texture}
    <T.Mesh
        onwheel={(e) => zoom(e)}
        onpointerdown={(e) => {
            dragging = true
            posX = e.nativeEvent.clientX
            posY = e.nativeEvent.clientY
        }}
        onpointerup={(e) => {dragging = false}}
        onpointerleave={(e) => {dragging = false}}
        onpointerout={(e) => {dragging = false}}
        onpointermove={(e) => handleDrag(e)}
    >
        <T.BoxGeometry args={[7, 4, 0]}/>
        <T.MeshBasicMaterial map={texture}/>
    </T.Mesh>
{/await}