<script lang="ts">
  import { onMount } from 'svelte';

  // Props with types
  export let src: string = '';
  export let alt: string = 'Interactive map';
  export let width: string = '100%';
  export let height: string = '500px';
  export let minZoom: number = 0.1;
  export let maxZoom: number = 5;
  export let initialZoom: number = 1;

  // Component state with types
  let container: HTMLDivElement;
  let image: HTMLImageElement;
  let zoom: number = initialZoom;
  let translateX: number = 0;
  let translateY: number = 0;
  let isDragging: boolean = false;
  let lastX: number = 0;
  let lastY: number = 0;

  // Handle mouse wheel for zooming
  function handleWheel(event: WheelEvent): void {
    event.preventDefault();

    const rect: DOMRect = container.getBoundingClientRect();
    const mouseX: number = event.clientX - rect.left;
    const mouseY: number = event.clientY - rect.top;

    const zoomFactor: number = 1.1;
    const delta: number = event.deltaY > 0 ? 1 / zoomFactor : zoomFactor;
    const newZoom: number = Math.min(Math.max(zoom * delta, minZoom), maxZoom);

    if (newZoom !== zoom) {
      // Calculate zoom point relative to current transform
      const zoomPointX: number = (mouseX - translateX) / zoom;
      const zoomPointY: number = (mouseY - translateY) / zoom;

      // Update zoom
      zoom = newZoom;

      // Adjust translation to keep zoom point under mouse
      translateX = mouseX - zoomPointX * zoom;
      translateY = mouseY - zoomPointY * zoom;
    }
  }

  // Handle mouse down for starting drag
  function handleMouseDown(event: MouseEvent): void {
    isDragging = true;
    lastX = event.clientX;
    lastY = event.clientY;
    container.style.cursor = 'grabbing';
  }

  // Handle mouse move for dragging
  function handleMouseMove(event: MouseEvent): void {
    if (!isDragging) return;

    const deltaX: number = event.clientX - lastX;
    const deltaY: number = event.clientY - lastY;

    translateX += deltaX;
    translateY += deltaY;

    lastX = event.clientX;
    lastY = event.clientY;
  }

  // Handle mouse up for ending drag
  function handleMouseUp(): void {
    isDragging = false;
    container.style.cursor = 'grab';
  }

  // Handle mouse leave to stop dragging if mouse leaves container
  function handleMouseLeave(): void {
    isDragging = false;
    container.style.cursor = 'grab';
  }

  // Reset view to initial state
  export function resetView(): void {
    zoom = initialZoom;
    translateX = 0;
    translateY = 0;
  }

  // Fit image to container
  export function fitToContainer(): void {
    if (!image || !container) return;

    const containerRect: DOMRect = container.getBoundingClientRect();

    const scaleX: number = containerRect.width / image.naturalWidth;
    const scaleY: number = containerRect.height / image.naturalHeight;

    zoom = Math.min(scaleX, scaleY);
    translateX = (containerRect.width - image.naturalWidth * zoom) / 2;
    translateY = (containerRect.height - image.naturalHeight * zoom) / 2;
  }

  onMount(() => {
    // Add global mouse event listeners for dragging
    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseup', handleMouseUp);

    // Set initial cursor
    container.style.cursor = 'grab';

    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
    };
  });
</script>

<div
  class="map-container"
  style="width: {width}; height: {height};"
  bind:this={container}
  on:wheel={handleWheel}
  on:mousedown={handleMouseDown}
  on:mouseleave={handleMouseLeave}
  role="presentation"
  aria-label="This is the world map"
>
  <img
    {src}
    {alt}
    class="map-image"
    style="transform: translate({translateX}px, {translateY}px) scale({zoom}); transform-origin: 0 0;"
    bind:this={image}
    draggable="false"
    on:load={fitToContainer}
  />
</div>

<style>
  .map-container {
    position: relative;
    overflow: hidden;
    border: 1px solid #ccc;
    user-select: none;
    background-color: #f5f5f5;
  }

  .map-image {
    display: block;
    max-width: none;
    max-height: none;
    transition: transform 0.1s ease-out;
  }

  .map-container:active {
    cursor: grabbing !important;
  }
</style>
