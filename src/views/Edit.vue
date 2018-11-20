<template>
    <form
        @submit="checkForm">
        <div>
            <h1>Editing entry: {{ entryId }}</h1>
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
    data() {
        return {
            editorConfig: {
                toolbar: ["bold", "italic", "heading", "|", "quote", "code", "unordered-list", "ordered-list", "|", "link", "image", "|", "preview"],
            },
            entryId: this.$route.params.entryId,
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
            // eslint-disable-next-line
            console.log("saving!");
            // reset this.$data.isDirty

            return true;
        }
    }
}
</script>
