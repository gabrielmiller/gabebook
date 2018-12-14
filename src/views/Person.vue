<template>
    <div>
        <h1>
            {{model.person.name}}
            <button
                class="link-button edit-pencil"
                type="button"
                v-if="!isEditing"
                v-on:click="toggleEdit">
                <i class="fa fa-pencil"></i>
            </button>
        </h1>

        <div v-if="!isEditing">
            <div class="person-details">
                <label
                    class="hover"
                    for="overview">
                    Overview
                </label>
                <input
                    class="invisible-toggle"
                    id="overview"
                    type="checkbox">
                <ul class="accordion ease-slide">
                    <li v-if="model.person.age">Age: {{model.person.age}}</li>
                    <li v-if="model.person.birthday">Born: {{model.person.birthday}}</li>
                    <li v-if="model.person.gender">Identifies as: {{model.person.gender}}</li>
                    <li v-if="model.person.knowFrom">Know from: {{model.person.knowFrom}}</li>
                    <li v-if="model.person.metPlace">Met at: {{model.person.metPlace}}</li>
                    <li v-if="model.person.metDate">Met on: {{model.person.metDate}}</li>
                    <li v-if="model.person.livesIn">Lives in: {{model.person.livesIn}}</li>
                    <li v-if="model.person.from">From: {{model.person.from}}</li>
                    <li v-if="model.person.studied">Studied {{model.person.studied}}</li>
                    <li v-if="model.person.college">Studied at {{model.person.college}}</li>
                </ul>
            </div>
            <div class="person-details">
                <label
                    class="hover"
                    for="profession">
                    Profession
                </label>
                <input
                    class="invisible-toggle"
                    id="profession"
                    type="checkbox">
                <ul class="accordion ease-slide">
                    <li v-if="model.person.jobTitle">Job: {{model.person.jobTitle}}</li>
                    <li v-if="model.person.jobDescription">Description: {{model.person.jobDescription}}</li>
                </ul>
            </div>
        </div>

        <div v-if="isEditing">
            <form v-on:submit="saveEdit">
                <!--
                <div class="input-wrapper">
                    <input id="test1" style="width:2em;" type="text" required>
                    <label for="test1">2em</label>
                </div>
                <div class="input-wrapper">
                    <input id="test2" style="width:4em;" type="text" required>
                    <label for="test2">4em</label>
                </div>
                <div class="input-wrapper">
                    <input id="test3" style="width:6em;" type="text" required>
                    <label for="test3">6em</label>
                </div>
                <div class="input-wrapper">
                    <input id="test4" style="width:8em;" type="text" required>
                    <label for="test4">8em</label>
                </div>
                <div class="input-wrapper">
                    <input id="test5" style="width:10em;" type="text" required>
                    <label for="test5">10em</label>
                </div>
                <div class="input-wrapper">
                    <input id="test6" style="width:12em;" type="text" required>
                    <label for="test6">12em</label>
                </div>
                <div class="input-wrapper">
                    <input id="test7" style="width:14em;" type="text" required>
                    <label for="test7">14em</label>
                </div>
                <div class="input-wrapper">
                    <input id="test8" style="width:16em;" type="text" required>
                    <label for="test8">16em</label>
                </div>
                <div class="input-wrapper">
                    <input id="test9" style="width:18em;" type="text" required>
                    <label for="test9">18em</label>
                </div>
                <div class="input-wrapper">
                    <input id="test10" style="width:20em;" type="text" required>
                    <label for="test10">20em</label>
                </div>
                -->
                <div class="input-wrapper">
                    <input id="name" type="text" required>
                    <label for="name">Name</label>
                </div>
                <div class="input-wrapper">
                    <input id="birthday" type="date">
                    <label for="birthday">Birthday</label>
                </div>
                <div class="input-wrapper">
                    <select id="gender">
                        <option value="" selected>-</option>
                        <option value="female">Female</option>
                        <option value="male">Male</option>
                    </select>
                    <label for="gender">Identifies as</label>
                </div>
                <div class="input-wrapper">
                    <input id="metAt" type="text">
                    <label for="metAt">Met at</label>
                </div>
                <button
                    class="primary-button save-button"
                    :disabled="isSaving"
                    type="submit">
                    <i class="fa fa-floppy-o"></i> Save
                </button>
            </form>
        </div>

        <div>
            <span>id: {{model.id}}</span>
            <pre style="white-space:pre-wrap;word-wrap:break-word;">{{JSON.stringify(model.person)}}</pre>
        </div>
    </div>
</template>

<script>
import mockData from '../mockData';

function loadPerson(personId) {
    let p = new Promise((resolve) => {
        setTimeout(() => {
            resolve(mockData.getPerson(personId));
        }, 1500);
    });

    return p;
}
export default {
    beforeRouteEnter(to, from, next) {
        loadPerson(to.params.personId).then((person => {
            next(vm => {
                vm.model.person = person;
            });
        }));
    },
    beforeRouteUpdate(to, from, next) {
        loadPerson(to.params.personId).then((person => {
            next(vm => {
                vm.model.person = person;
            });
        }));
    },
    created() {
        this.people = this.$parent.people;
    },
    computed: {
        isEditing: function() {
            return this.state.isEditing;
        },
        isNew: function() {
            return this.state.isNew;
        },
        isSaving: function() {
            return this.state.isSaving;
        }
    },
    data() {
        return {
            model: {
                people: [],
                person: {},
                id: this.$route.params.personId,
            },
            state: {
                isEditing: false,
                isNew: false,
                isSaving: false,
            }
        }
    },
    methods: {
        saveEdit: function(event) {
            event.preventDefault();
            this.state.isSaving = true;

            let p = new Promise((resolve) => {
                setTimeout(() => {
                    this.state.isEditing = false;
                    this.state.isSaving = false;
                    resolve();
                }, 1500);
            });

            return p;
        },
        toggleEdit: function() {
            this.state.isEditing = true;
        }
    }
}
</script>