document.addEventListener("DOMContentLoaded", function () {
    form1 = document.getElementById("form1");
    form2 = document.getElementById("form2");
    form3 = document.getElementById("form3");
    form4 = document.getElementById("form4");
    form5 = document.getElementById("form5");
    form6 = document.getElementById("form6");

    file1 = document.getElementById("file1");
    file2 = document.getElementById("file2");
    file3 = document.getElementById("file3");
    file4 = document.getElementById("file4");
    file5 = document.getElementById("file5");
    file6 = document.getElementById("file6");

    // auto submit form
    file1.onchange = function () {
        setTimeout(() => {
            form1.submit();
        }, 500);
    };
    file2.onchange = function () {
        setTimeout(() => {
            form2.submit();
        }, 500);
    };
    file3.onchange = function () {
        setTimeout(() => {
            form3.submit();
        }, 500);
    };
    file4.onchange = function () {
        setTimeout(() => {
            form4.submit();
        }, 500);
    };
    file5.onchange = function () {
        setTimeout(() => {
            form5.submit();
        }, 500);
    };
    file6.onchange = function () {
        setTimeout(() => {
            form6.submit();
        }, 500);
    };
});
