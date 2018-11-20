<template>
    <div>
        <ul>
            <li v-for="person in people" :key="person.id">
                <router-link :to="{ name: 'Person', params: { personId: person.id }}">
                    <span>{{ person.name }}</span>
                </router-link>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    created() {
        this.people = this.$parent.people;
    },
    data() {
        return {
            people: []
        };
    }
}
</script>