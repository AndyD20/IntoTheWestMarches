<script lang="ts">
    import Map from '$lib/components/Map/map.svelte';
    import MapImage from '$lib/assets/The_Northern_Empire.png'

    // Type for the Map component instance
    interface MapComponent {
        resetView(): void;

        fitToContainer(): void;
    }

    let mapComponent: MapComponent;

    // Example with typed props
    const mapProps = {
        src: MapImage,
        height: '800px',
        minZoom: 0.8,
        maxZoom: 3,
        initialZoom: 1
    };

    function handleResetClick(): void {
        mapComponent.resetView();
    }

    function handleFitClick(): void {
        mapComponent.fitToContainer();
    }
</script>

<Map
  {...mapProps}
  bind:this={mapComponent}
/>

<button on:click={handleResetClick}>Reset</button>
<button on:click={handleFitClick}>Fit to Screen</button>