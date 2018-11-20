<template>
    <div>
        Person
        <span> {{personId}} </span>
    </div>
</template>

<script>
export default {
    created() {// eslint-disable-next-line
        console.log("created");
        this.people = this.$parent.people;
    },
    data() {
        return {
            people: [],
            personId: this.$route.params.personId,
        }
    },
}
</script>