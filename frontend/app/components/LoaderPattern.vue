<template>
    <svg viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
        <path d="M8 16A8 8 0 118 0v2a6 6 0 106 6h2a8 8 0 01-8 8z" fill="currentColor" fill-rule="evenodd" />
    </svg>
</template>

<style scoped>
svg {
    animation: loader-rotate .5s infinite linear;
}

@keyframes loader-rotate {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}
</style>