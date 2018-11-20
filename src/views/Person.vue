<template>
    <div>
        <h1>
            {{person.name}}
            <router-link :to="{ name: 'Edit Person', params: { personId: person.id }}">
                <i class="super fa fa-pencil"></i>
            </router-link>
        </h1>
        <div class="person-details">
            <label
                for="overview">
                Overview
            </label>
            <input
                checked="true"
                class="invisible-toggle"
                id="overview"
                type="checkbox">
            <ul class="accordion ease-slide accordion">
                <li v-if="person.age">Age: {{person.age}}</li>
                <li v-if="person.gender">Identifies as: {{person.gender}}</li>
                <li v-if="person.knowFrom">Know from: {{person.knowFrom}}</li>
                <li v-if="person.metPlace">Met at: {{person.metPlace}}</li>
                <li v-if="person.metDate">Met on: {{person.metDate}}</li>
                <li v-if="person.livesIn">Lives in: {{person.livesIn}}</li>
                <li v-if="person.from">From: {{person.from}}</li>
                <li v-if="person.studied">Studied {{person.studied}}</li>
                <li v-if="person.college">Studied at {{person.college}}</li>
            </ul>
        </div>
        <div class="person-details">
            <label
                for="profession">
                Profession
            </label>
            <input
                checked="true"
                class="invisible-toggle"
                id="profession"
                type="checkbox">
            <ul class="accordion ease-slide accordion">
                <li v-if="person.jobTitle">Job: {{person.jobTitle}}</li>
                <li v-if="person.jobDescription">Description: {{person.jobDescription}}</li>
            </ul>
        </div>
        <span>id: {{personId}}</span>
        <pre style="white-space:pre-wrap;">{{JSON.stringify(person)}}</pre>
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
        loadPerson(to.params.personId).then((person) => {
            next(vm => {
                vm.person = person;
            });
        });
    },
    beforeRouteUpdate(to, from, next) {
        loadPerson(to.params.personId).then((person) => {
            next(vm => {
                vm.person = person;
            });
        });
    },
    created() {
        this.people = this.$parent.people;
    },
    data() {
        return {
            people: [],
            person: {},
            personId: this.$route.params.personId,
        }
    },
}
</script>