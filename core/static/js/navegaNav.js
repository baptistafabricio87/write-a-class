function navegaNav() {
    // Obtém a URL atual da página
    var currentUrl = window.location.href;

    // Obtém todos os elementos de navegação
    var navItems = document.querySelectorAll(".navbar-nav .nav-link");

    // Itera sobre cada elemento de navegação
    navItems.forEach(function (item) {
        // Obtém o valor do atributo "href" do item de navegação
        var itemUrl = item.getAttribute("href");

        // Verifica se a URL atual coincide com o valor do atributo "href"
        if (currentUrl.includes(itemUrl)) {
            // Adiciona a classe "active" ao item de navegação
            item.classList.add("activeNav");
        } else {
            // Remove a classe "active" de outros itens de navegação
            item.classList.remove("activeNav");
        }
    });
}



document.addEventListener("DOMContentLoaded", function () {
    navegaNav(); // Chama a função navegaNav() aqui

});
