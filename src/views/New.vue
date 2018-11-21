<template>
    <form
        @submit="checkForm">
        <div>
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
            <input
                @keydown="isDirty = true"
                placeholder="Regarding"
                type="text"
                v-model="regarding">
            <markdown-editor
                :highlight="false"
                :configs="editorConfig"
                @keydown="isDirty = true"
                v-model="post">
            </markdown-editor>
        </div>
        <button class="primary-button save-button" type="submit"><i class="fa fa-floppy-o"></i> Save</button>
    </form>
</template>

<script>
export default {
    data() {
        return {
            editorConfig: {
                toolbar: ["bold", "italic", "heading", "|", "quote", "code", "unordered-list", "ordered-list", "|", "link", "image", "|", "preview"],
            },
            isDirty: false,
            regarding: [],
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
