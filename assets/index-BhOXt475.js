(function(){const s=document.createElement("link").relList;if(s&&s.supports&&s.supports("modulepreload"))return;for(const e of document.querySelectorAll('link[rel="modulepreload"]'))r(e);new MutationObserver(e=>{for(const t of e)if(t.type==="childList")for(const c of t.addedNodes)c.tagName==="LINK"&&c.rel==="modulepreload"&&r(c)}).observe(document,{childList:!0,subtree:!0});function o(e){const t={};return e.integrity&&(t.integrity=e.integrity),e.referrerPolicy&&(t.referrerPolicy=e.referrerPolicy),e.crossOrigin==="use-credentials"?t.credentials="include":e.crossOrigin==="anonymous"?t.credentials="omit":t.credentials="same-origin",t}function r(e){if(e.ep)return;e.ep=!0;const t=o(e);fetch(e.href,t)}})();function a(){return`<div class="Main">
        <h1>Тестовое приложение</h1>
        <img src="./src/assets/closeup-shot-sheep.avif" alt="sheep photo" class="main-image">
        <p></p>
        <button class="btn f-btn">Тест отправки данных</button>
    </div>
    <form class="test-form">
        <input type="text" placeholder="Введите заголовок" class="title-inp">
        <input type="text" placeholder="Введите описание" class="desc-inp">
        <input type="text" placeholder="Введите текст" class="text-inp">
        <button class="btn s-btn">Отправить</button>
    </form>`}function u(){return`<div class="Main">
        <h1>Второй экран</h1>
        <img src="./src/assets/closeup-shot-sheep.avif" alt="sheep photo" class="main-image">`}function l(n){i&&(i.innerHTML=n==="start"?a():u())}const d=window.Telegram.WebApp,i=document.querySelector("#app");l("start");const p=document.querySelector(".f-btn"),f=document.querySelector(".s-btn"),m=document.querySelector(".Main"),y=document.querySelector(".test-form");p.addEventListener("click",()=>{m.style.display="none",y.style.display="block"});f.addEventListener("click",()=>{const n=document.querySelector(".title-inp"),s=document.querySelector(".desc-inp"),o=document.querySelector(".text-inp"),r={title:n.value,desc:s.value,text:o.value};d.sendData(JSON.stringify(r)),l("end")});
