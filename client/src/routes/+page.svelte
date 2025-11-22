<script>
    import { resolve } from '$app/paths';
    import mapImage from '$lib/assets/placeholder_map.png';
</script>

<div class="min-h-screen bg-slate-900 text-slate-200 font-sans selection:bg-amber-500 selection:text-slate-900">

    <header class="relative overflow-hidden">
        <div class="absolute inset-0 opacity-20">
            <img src={mapImage} alt="Background Map" class="w-full h-full object-cover grayscale opacity-50" />
            <div class="absolute inset-0 bg-gradient-to-b from-slate-900/80 via-slate-900/90 to-slate-900"></div>
        </div>

        <div class="relative max-w-7xl mx-auto px-6 pt-24 pb-16 sm:px-12 sm:pt-32 lg:px-16 text-center">
            <h1 class="text-5xl sm:text-7xl font-bold tracking-tight text-amber-500 drop-shadow-lg" style="font-family: 'Almendra', serif;">
                Into The West Marches
            </h1>
            <p class="mt-6 text-lg sm:text-2xl leading-8 text-slate-300 max-w-3xl mx-auto">
                The frontier is wild, the dungeons are deep, and the taverns... well, the ale is lukewarm. <br class="hidden sm:inline">Chart your path through the unknown.
            </p>
            <div class="mt-10 flex items-center justify-center gap-x-6">
                <a
                    href={resolve("/map")}
                    class="rounded-md bg-amber-600 px-8 py-4 text-lg font-semibold text-white shadow-sm hover:bg-amber-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-amber-600 transition-all transform hover:-translate-y-1 border border-amber-400/30"
                >
                    Open the Game Map
                </a>
                <a href="#about" class="text-sm font-semibold leading-6 text-slate-300 hover:text-white transition-colors">
                    Learn more <span aria-hidden="true">→</span>
                </a>
            </div>
        </div>
    </header>

    <section class="py-16 sm:py-24 bg-slate-800/50 border-y border-slate-700/50">
        <div class="mx-auto max-w-7xl px-6 lg:px-8">
            <div class="mx-auto max-w-2xl lg:text-center">
                <h2 class="text-base font-semibold leading-7 text-amber-500">Explore • Expand • Exploit</h2>
                <p class="mt-2 text-3xl font-bold tracking-tight text-slate-100 sm:text-4xl" style="font-family: 'Almendra', serif;">
                    No More Scribbling on Napkins
                </p>
                <p class="mt-6 text-lg leading-8 text-slate-400">
                    Stop relying on the Bard's memory (we all know they're making it up). Into The West Marches provides a persistent, interactive world for your entire party.
                </p>
            </div>
            <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-none">
                <dl class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-16 lg:max-w-none lg:grid-cols-3">
                    <div class="flex flex-col items-start">
                        <div class="rounded-lg bg-slate-900 p-2 ring-1 ring-white/10">
                           <span class="text-2xl">🗺️</span>
                        </div>
                        <dt class="mt-4 font-semibold text-white text-xl" style="font-family: 'Almendra', serif;">Interactive Exploration</dt>
                        <dd class="mt-2 leading-7 text-slate-400">
                            Zoom, pan, and drag your way across the Northern Empire. Find the path of least resistance, or the one with the most loot.
                        </dd>
                    </div>
                    <div class="flex flex-col items-start">
                        <div class="rounded-lg bg-slate-900 p-2 ring-1 ring-white/10">
                            <span class="text-2xl">PF</span>
                        </div>
                        <dt class="mt-4 font-semibold text-white text-xl" style="font-family: 'Almendra', serif;">Persistent Frontiers</dt>
                        <dd class="mt-2 leading-7 text-slate-400">
                            Did you find a cave full of angry owlbears? Mark it! Double-click anywhere on the map to drop a pin so your future self (or next character) knows where <em>not</em> to go.
                        </dd>
                    </div>
                    <div class="flex flex-col items-start">
                        <div class="rounded-lg bg-slate-900 p-2 ring-1 ring-white/10">
                            <span class="text-2xl">📜</span>
                        </div>
                        <dt class="mt-4 font-semibold text-white text-xl" style="font-family: 'Almendra', serif;">Living Chronicle</dt>
                        <dd class="mt-2 leading-7 text-slate-400">
                            A shared history for every player. See where others have ventured and coordinate your expeditions. It's like a guild hall, but with fewer brawls.
                        </dd>
                    </div>
                </dl>
            </div>
        </div>
    </section>

    <section id="about" class="relative isolate overflow-hidden px-6 py-24 sm:py-32 lg:overflow-visible lg:px-0">
        <div class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 lg:mx-0 lg:max-w-none lg:grid-cols-2 lg:items-start lg:gap-y-10">
            <div class="lg:col-span-2 lg:col-start-1 lg:row-start-1 lg:mx-auto lg:grid lg:w-full lg:max-w-7xl lg:grid-cols-2 lg:gap-x-8 lg:px-8">
                <div class="lg:pr-4">
                    <div class="lg:max-w-lg">
                        <p class="text-base font-semibold leading-7 text-amber-500">The Mission</p>
                        <h1 class="mt-2 text-3xl font-bold tracking-tight text-slate-100 sm:text-4xl" style="font-family: 'Almendra', serif;">A Map for the Mad & The Brave</h1>
                        <p class="mt-6 text-xl leading-8 text-slate-300">
                            Roleplaying games are about imagination, but let's be honest: sometimes you just need to know exactly how far it is to the nearest safe haven.
                        </p>
                    </div>
                </div>
            </div>

            <div class="-ml-12 -mt-12 p-12 lg:top-4 lg:col-start-2 lg:row-span-2 lg:row-start-1 lg:overflow-hidden">
                <img
                    class="w-[36rem] max-w-none rounded-xl bg-slate-900 shadow-xl ring-1 ring-gray-400/10 lg:w-[48rem]"
                    src={mapImage}
                    alt="Detail of the game map"
                />
            </div>

            <div class="lg:col-span-2 lg:col-start-1 lg:row-start-2 lg:mx-auto lg:grid lg:w-full lg:max-w-7xl lg:grid-cols-2 lg:gap-x-8 lg:px-8">
                <div class="lg:pr-4">
                    <div class="max-w-xl text-base leading-7 text-slate-400 lg:max-w-lg">
                        <p>
                            Into The West Marches was built to solve a simple problem: "Wait, where was that goblin camp again?"
                        </p>
                        <p class="mt-4">
                            In a West Marches style campaign, the world is vast, the roster of heroes rotates, and information is the most valuable currency. This tool serves as your cartographer's table. It allows you to:
                        </p>
                        <ul role="list" class="mt-8 space-y-8 text-slate-400">
                            <li class="flex gap-x-3">
                                <span class="mt-1 h-5 w-5 flex-none text-amber-500">⚔️</span>
                                <span><strong class="font-semibold text-slate-100">Track Dangers:</strong> Mark boss locations, traps, and zones of wild magic.</span>
                            </li>
                            <li class="flex gap-x-3">
                                <span class="mt-1 h-5 w-5 flex-none text-amber-500">💎</span>
                                <span><strong class="font-semibold text-slate-100">Catalog Loot:</strong> Found a dungeon you couldn't clear? Mark it for later when you've leveled up.</span>
                            </li>
                            <li class="flex gap-x-3">
                                <span class="mt-1 h-5 w-5 flex-none text-amber-500">🍺</span>
                                <span><strong class="font-semibold text-slate-100">Plan Expeditions:</strong> Look at the empty spots on the map and decide where to go next.</span>
                            </li>
                        </ul>
                        <p class="mt-10">
                            So grab your sword, ready your spells, and don't forget to update the map if you survive.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer class="bg-slate-950 py-12 border-t border-slate-800">
        <div class="mx-auto max-w-7xl px-6 lg:px-8 flex flex-col items-center justify-center">
            <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl mb-6" style="font-family: 'Almendra', serif;">Ready to venture forth?</h2>
            <a
                href={resolve("/map")}
                class="rounded-full bg-slate-100 px-6 py-3 text-base font-semibold text-slate-900 shadow-sm hover:bg-slate-200 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white transition-colors"
            >
                Enter the Map
            </a>
            <p class="mt-8 text-xs leading-5 text-slate-500 text-center">
                &copy; 2025 Into The West Marches. Beware of dragons. <br> Made with SvelteKit & Threlte.
            </p>
        </div>
    </footer>
</div>
