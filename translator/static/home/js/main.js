const input = document.querySelector(".input");
const output = document.querySelector(".output");
const submit = document.querySelector(".submit");
const from_language = document.querySelector("#from-language");
const to_language = document.querySelector("#to-language");

submit.addEventListener("click", () => {
  const data = {
    input: input.value.trim(),
    from: from_language.value,
    to: to_language.value,
  };
  submit.disabled = true;
  axios
    .post("translate/", data)
    .then((response) => {
      submit.disabled = false;
      output.value = response.data.output;
    })
    .catch((error) => {
      alert(error.response.data.error);
      submit.disabled = false;
    });
});
