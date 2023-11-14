<template>
    <v-container
    class="d-flex align-center justify-center"
    style="height:100%"
    >
        <v-container>
            <v-row
            class="d-flex justify-center my-4 pa-0"
            v-for="(word, index) in game_data"
            :key="index"
            >
                <char
                v-for="(character, index) in word"
                :key="index"
                :character="character.character"
                :check="character.check"
                class="my-0 mx-2"
                />
            </v-row>
        </v-container>

        <v-text-field
        ref="input"
        @blur="$refs.input.focus()"
        v-model="writing"
        style="position:fixed;top:100%;left:100%;"
        :maxlength="level"
        />

        <v-container
        class="message-container d-flex align-center justify-center"
        v-if="won || lose"
        >
            <v-container
            style="width:70%"
            v-show="won"
            >
                <v-row
                class="d-flex justify-center"
                >
                    <span
                    class="message"
                    >
                        Congratulations!!!
                    </span>
                </v-row>

                <v-row
                class="d-flex justify-end"
                >
                    You won the game...
                </v-row>
            </v-container>

            <v-container
            style="width:70%"
            v-show="lose"
            >
                <v-row
                class="d-flex justify-center"
                >
                    <span
                    class="message"
                    >
                        We sorry :(
                    </span>
                </v-row>

                <v-row
                class="d-flex justify-end"
                >
                    You lose the game...
                </v-row>
            </v-container>
        </v-container>
    </v-container>
</template>

<script>
import char from '../components/char.vue';
export default {
    components: { char },
    loading: false,
    name: "game",
    data() {
        return {
            game_data: [],
            row: 0,
            writing: "",
            level: 0,
            won: false,
            lose: false,
        }
    },
    watch: {
        writing() {
            this.updateGame();
        }
    },
    methods: {
        updateGame() {
            if (this.writing.length == this.level) {
                this.$axios.post("/check_word", {"word": this.writing, progress: false})
                .then((response) => {
                    this.won = true;
                    for (let i=0; i<this.level; i++) {
                        this.game_data[this.row][i].check = response.data.check[i];
                        if (response.data.check[i] != "right") {
                            this.won = false;
                        }
                    }
                    if (this.row == this.level-1 && !this.won) {
                        this.lose = true;
                    }
                    else {
                        this.row++;
                        this.writing="";
                    }
                })
            }
            if (this.row < this.level) {
                for (let i=0; i<this.level; i++) {
                    if (i < this.writing.length) {
                        this.game_data[this.row][i].character = this.writing.charAt(i);
                    }
                    else {
                        this.game_data[this.row][i].character = " ";
                    }
                }
            }
        }
    },
    mounted() {
        this.$axios.get("/get_difficulty")
        .then((response) => {
            this.level = response.data.difficulty;
            for (let i=0; i<response.data.difficulty; i++) {
                let c = [];
                for (let i=0; i<this.level; i++) {
                    c.push({
                        "character": " ",
                        "check": ""
                    });
                }
                this.game_data.push(c);
            }
            this.$refs.input.focus();
        })
        .catch((error) => {
            this.$router.push({path:"/"});
        })
    },
}
</script>

<style scoped>
.message-container {
    position:fixed;
    height:100%;
    width:100%;
    z-index:1;
    backdrop-filter:blur(2px);
}
.message {
    font-weight: 900;
    font-size: 6vw;
}
</style>
