<template>
    <div>
        <div v-for="person in people">
            <span>{{ person.name }}</span>
        </div>
    </div>
</template>

<script>
export default {
    created() {// eslint-disable-next-line
        console.log("created!", this);
    },
    data() {
        return {
            people: [
                { id: 1, name: 'Gerb Merrer' },
                { id: 2, name: 'bonecrusher' }
            ]
        };
    }
}
</script>