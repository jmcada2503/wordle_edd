<template>
    <v-container
    class="d-flex align-center justify-center"
    style="height:100%"
    >
        <v-container
        style="width:500px;"
        >
            <v-row>
                <span
                style="font-size:24px;font-weight:500;"
                >
                    Let's start playing
                </span>
            </v-row>

            <v-row
            class="d-flex justify-center"
            >
                <span
                style="font-size:40px;font-weight:900;"
                >
                    CustomWordle
                </span>
            </v-row>

            <v-row
            class="d-flex justify-end"
            >
                <span
                style="font-size:24px;font-weight:500;"
                >
                    select difficulty...
                </span>
            </v-row>
            
            <v-row
            class="mt-16"
            >
                <v-btn
                outlined
                class="py-6"
                style="width:100%"
                @click="selectDifficulty(4)"
                >
                    4 letters
                </v-btn>
            </v-row>

            <v-row
            class="mt-8"
            >
                <v-btn
                outlined
                class="py-6"
                style="width:100%"
                @click="selectDifficulty(5)"
                >
                    5 letters
                </v-btn>
            </v-row>

            <v-row
            class="mt-8"
            >
                <v-btn
                outlined
                class="py-6"
                style="width:100%"
                @click="selectDifficulty(6)"
                >
                    6 letters
                </v-btn>
            </v-row>

            <v-row
            class="mt-8"
            >
                <v-btn
                outlined
                class="py-6"
                style="width:100%"
                @click="selectDifficulty(7)"
                >
                    7 letters
                </v-btn>
            </v-row>

            <v-row
            class="mt-8"
            >
                <v-btn
                outlined
                class="py-6"
                style="width:100%"
                @click="selectDifficulty(8)"
                >
                    8 letters
                </v-btn>
            </v-row>
        </v-container>
    </v-container>
</template>

<script>
export default {
  name: 'start',
  methods: {
    selectDifficulty(level) {
        this.$axios.post("/set_difficulty", {"difficulty":level})
        .then((response) => {
            this.$router.push({path:"/game"})
        })
    }
  }
}
</script>
