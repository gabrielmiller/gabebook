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
                Is editing!
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