<template>
    <v-container
    dark
    class="container d-flex justify-center align-center"
    :class="check"
    >
        <span
        style="text-transform:uppercase"
        >
            {{ character }}
        </span>
    </v-container>
</template>

<script>
export default {
    name: "char",
    props: [
        "character",
        "check",
    ],
    data() {
        return {

        }
    },
}
</script>

<style scoped>
.container {
    height: 7.5vh;
    width: 7.5vh;
    border: 2px solid white;
    border-radius:4px;
}
.right {
    background-color: #4E9F3D;
    border-width: 0px !important;
}
.wrong {
    background-color: #950101;
    border-width: 0px !important;
}
.medium {
    background-color: #b5ae2d;
    border-width: 0px !important;
}
</style>
