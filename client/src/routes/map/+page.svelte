<script lang="ts">
    import {Canvas} from "@threlte/core";
    import Map from '$lib/components/Map/map.svelte';
    import type {PageProps} from "./$types";

    let {data}: PageProps = $props();
</script>

<div>
    This is the application
</div>

<Canvas>
    <Map marker_data={data}/>
</Canvas>
