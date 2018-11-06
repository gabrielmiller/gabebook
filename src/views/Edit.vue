<template>
    <form
        @submit="checkForm">
        <div>
            <h1>Editing entry: {{ id }}</h1>
            <input
                @keydown="isDirty = true"
                placeholder="Title"
                required
                type="text"
                v-model="title">
            <input
            @keydown="isDirty = true"
                placeholder="Tags"
                type="text"
                v-model="tags">
            <markdown-editor
                :highlight="false"
                :configs="editorConfig"
                @keydown="isDirty = true"
                v-model="post">
            </markdown-editor>
        </div>
        <button type="submit">Save</button>
    </form>
</template>

<script>
export default {
    beforeRouteLeave(to, from, next) {
        let leave = true;

        if (this.$data.isDirty) {
            leave = confirm("Are you sure you want to leave?");
        }

        if (leave) {
            next();
        }
    },
    data() {
        return {
            editorConfig: {
                toolbar: ["bold", "italic", "heading", "|", "quote", "code", "unordered-list", "ordered-list", "|", "link", "image", "|", "preview"],
            },
            id: this.$route.params.id,
            isDirty: false,
            tags: "",
            title: "",
            post: "",
        }
    },
    methods: {
        checkForm($event) {
            $event.preventDefault();

            if (this.$data.title.length === 0) {
                return false;
            }

            if (this.$data.post.length === 0) {
                return false;
            }

            console.log("saving!");
            // reset this.$data.isDirty

            return true;
        }
    }
}
</script>
