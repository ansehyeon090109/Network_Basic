var n = 0
var num = document.getElementById("num")
var plus = document.getElementById("plus")
var forwarding = document.getElementById("forwarding")

plus.addEventListener("click", function() {
    n += 1
    num.textContent = n
})