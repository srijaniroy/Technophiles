var script = document.createElement("script");
script.type = "text/javascript";
script.src =
  "https://cdn.tiny.cloud/1/gjqojwu7li8z9bscgkkoqoz5al2bho6iko223ydcunemqk81/tinymce/7/tinymce.min.js";
document.head.appendChild(script);

script.onload = function () {
  tinymce.init({
    selector: "#id_content",
    height: 600,
    plugins: [
      "anchor",
      "autolink",
      "charmap",
      "codesample",
      "emoticons",
      "image",
      "link",
      "lists",
      "media",
      "searchreplace",
      "table",
      "visualblocks",
      "wordcount",
      "checklist",
      "mediaembed",
      "casechange",
      "export",
      "formatpainter",
      "pageembed",
      "a11ychecker",
      "tinymcespellchecker",
      "permanentpen",
      "powerpaste",
      "advtable",
      "advcode",
      "editimage",
      "advtemplate",
      "ai",
      "mentions",
      "tinycomments",
      "tableofcontents",
      "footnotes",
      "mergetags",
      "autocorrect",
      "typography",
      "inlinecss",
      "markdown",
    ],
    toolbar:
      "undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table mergetags | addcomment showcomments | spellcheckdialog a11ycheck typography | align lineheight | checklist numlist bullist indent outdent | emoticons charmap | removeformat",
    tinycomments_mode: "embedded",
    tinycomments_author: "Author name",
    mergetags_list: [
      { value: "First.Name", title: "First Name" },
      { value: "Email", title: "Email" },
    ],
    ai_request: (request, respondWith) =>
      respondWith.string(() =>
        Promise.reject("See docs to implement AI Assistant")
      ),
  });
};
