<script lang="ts">
	import { T, useThrelte } from '@threlte/core';
	import { useTexture, interactivity, SVG, HTML } from '@threlte/extras';
	import WorldMap from '$lib/assets/The_Northern_Empire.png';
	import MapPinIcon from '$lib/assets/map-pin.svg';
	import type { Marker, MarkerResponse } from '$lib/interfaces/marker';
	import {
		MapIcon as MapPin,
		HomeIcon as Home,
		FlagIcon as Flag,
		TargetIcon as Target,
		AnchorIcon as Anchor
	} from 'svelte-feather-icons';

	let { marker_data } = $props();
	let existing_markers = $state(marker_data);

	interactivity();

	let distance = $state(5);
	let dragging = $state(false);
	let posX = $state(0);
	let posY = $state(0);

	let cameraX = $state(0);
	let cameraY = $state(0);

	let markers = $state<Marker[]>([]);

	let menuVisible = $state(false);
	let pendingMarkerPosition = $state({ x: 0, y: 0 });

	const markerTypes = [
		{ type: 'default', icon: MapPin, label: 'Default' },
		{ type: 'home', icon: Home, label: 'Home' },
		{ type: 'flag', icon: Flag, label: 'Flag' },
		{ type: 'target', icon: Target, label: 'Target' },
		{ type: 'anchor', icon: Anchor, label: 'Anchor' }
	];

	const { renderer } = useThrelte();

	$effect(() => {
		if (renderer?.domElement) {
			renderer.domElement.style.cursor = dragging ? 'grabbing' : 'pointer';
		}
	});

	const zoom = (e: any) => {
		distance += e.nativeEvent.deltaY / 1000;
	};

	const handleDrag = (e: any) => {
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

	const handleOnDblClick = (e: any) => {
		pendingMarkerPosition = { x: e.point.x, y: e.point.y };
		menuVisible = true;
	};

	const selectMarkerType = async (type: string) => {
		menuVisible = false;
		const { x, y } = pendingMarkerPosition;

		// Optimistic update
		let newMarker: Marker = {
			id: crypto.randomUUID(), // Temporary ID
			posX: x,
			posY: y,
			type: type
		};
		markers.push(newMarker);

		const params = new URLSearchParams({
			pos_x: x.toString(),
			pos_y: y.toString(),
			type: type
		}).toString();

		try {
			const response = await fetch('http://localhost:5000/markers?' + params, { method: 'POST' });
			if (!response.ok) {
				console.error('Failed to save marker:', response);
			}
		} catch (error) {
			console.error('Error saving marker:', error);
		}
	};

	$effect(() => {
		if (existing_markers) {
			const existing_ids = new Set(markers.map((m) => m.id));

			const markers_to_add: Marker[] = [];
			existing_markers.markers.forEach((marker: MarkerResponse) => {
				if (!existing_ids.has(marker.id)) {
					markers_to_add.push({
						id: marker.id,
						posX: marker.pos_x,
						posY: marker.pos_y,
						type: marker.type || 'default'
					});
				}
			});

			if (markers_to_add.length > 0) {
				markers.push(...markers_to_add);
			}
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
		onwheel={(e: any) => zoom(e)}
		onpointerdown={(e: any) => {
			dragging = true;
			posX = e.nativeEvent.clientX;
			posY = e.nativeEvent.clientY;
		}}
		onpointerup={endDrag}
		onpointerleave={endDrag}
		onpointerout={endDrag}
		onpointermove={(e: any) => handleDrag(e)}
		ondblclick={handleOnDblClick}
	>
		<T.BoxGeometry args={[7, 4, 0]} />
		<T.MeshBasicMaterial map={texture} />
	</T.Mesh>
{/await}

{#each markers as marker (marker.id)}
	{@const Icon = markerTypes.find((t) => t.type === marker.type)?.icon || MapPin}
	<T.Group position.x={marker.posX} position.y={marker.posY} position.z={0.0001}>
		<HTML transform pointerEvents="none">
			<div class="text-red-600">
				<Icon size="6" />
			</div>
		</HTML>
	</T.Group>
{/each}

{#if menuVisible}
	<T.Group
		position.x={pendingMarkerPosition.x}
		position.y={pendingMarkerPosition.y}
		position.z={0.1}
	>
		<HTML transform>
			<div class="flex flex-col rounded bg-white p-2 shadow-lg">
				<div class="text-[0.5rem] font-bold text-gray-700">Select Marker</div>
				<div class="grid grid-cols-3">
					{#each markerTypes as { type, icon: Icon, label }}
						<button
							class="flex flex-col items-center justify-center rounded p-2 hover:bg-gray-100"
							onclick={() => selectMarkerType(type)}
							aria-label={label}
						>
							<Icon size="8" />
						</button>
					{/each}
				</div>
				<button
					class="mt-2 w-full rounded bg-gray-200 px-2 py-1 text-[0.5rem] hover:bg-gray-300"
					onclick={() => (menuVisible = false)}
				>
					Cancel
				</button>
			</div>
		</HTML>
	</T.Group>
{/if}
