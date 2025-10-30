<script lang="ts">
    import {Canvas} from "@threlte/core";
    import Map from '$lib/components/Map/map.svelte';
    import type {PageProps} from "./$types";
    import {resolve} from "$app/paths";

    let {data}: PageProps = $props();
</script>

<div class="bg-gray-800 overflow-x-hidden">
    <div>
        This is the application
    </div>

    <a href={resolve("/")}>Click here to return to the main menu</a>

    <Canvas>
        <Map marker_data={data}/>
    </Canvas>
</div>

