<template>
    <div class="div">
      <div class="div-2">
        <div class="column">
          <div class="div-3">
            <div class="div-4">
              <div class="div-5">Olá, bem vindo Usuário!</div>
              <div class="div-6">
                <img
                  loading="lazy"
                  src="https://cdn.builder.io/api/v1/image/assets/TEMP/7382b4ee-7208-42fd-bd82-b602ff0c4756?"
                  class="img"
                /><img
                  loading="lazy"
                  src="https://cdn.builder.io/api/v1/image/assets/TEMP/070336dd-b0f5-48a0-a45b-c3c43df3ea46?"
                  class="img-2"
                />
              </div>
            </div>
            <div class="div-7">CADASTRO</div>
            <div class="div-8">ESTOQUE</div>
            <div class="div-9">VENDAS</div>
            <div class="div-10">COMPRAS</div>
            <div class="div-11">CONFIGURAÇÕES</div>
          </div>
        </div>
        <div class="column-2">
          <div class="div-12">
            <div class="div-13">
              <img
                loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/6ab8db63-4b2b-450a-97c2-990dcc1bc8bc?"
                class="img-3"
              />
              <div class="div-14">ESTOQUE</div>
            </div>
            <div class="div-15">
              <div class="div-16">
                <div class="column">
                  <div class="div-17">
                    <img
                      loading="lazy"
                      srcSet="..."
                      class="img-4"
                    />
                    <div class="div-18">769ml</div>
                  </div>
                </div>
                <div class="column-3">
                  <div class="div-19">
                    <img
                      loading="lazy"
                      srcSet="..."
                      class="img-5"
                    />
                    <div class="div-20">314ml</div>
                  </div>
                </div>
                <div class="column-4">
                  <div class="div-21">
                    <img
                      loading="lazy"
                      srcSet="..."
                      class="img-6"
                    />
                    <div class="div-22">147ml</div>
                  </div>
                </div>
                <div class="column-5">
                  <div class="div-23">
                    <img
                      loading="lazy"
                      srcSet="..."
                      class="img-7"
                    />
                    <div class="div-24">884ml</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  
  
  <style scoped>
  .div {
    background-color: #9c9c9c;
    padding: 0 7px 0 8px;
  }
  .div-2 {
    gap: 20px;
    display: flex;
  }
  @media (max-width: 991px) {
    .div-2 {
      flex-direction: column;
      align-items: stretch;
      gap: 0px;
    }
  }
  .column {
    display: flex;
    flex-direction: column;
    line-height: normal;
    width: 25%;
    margin-left: 0px;
  }
  @media (max-width: 991px) {
    .column {
      width: 100%;
    }
  }
  .div-3 {
    border-radius: 20px;
    background-color: #373737;
    display: flex;
    width: 100%;
    flex-direction: column;
    margin: 7px auto 0;
    padding: 9px 18px 433px 22px;
  }
  @media (max-width: 991px) {
    .div-3 {
      margin-top: 14px;
      padding: 0 0 100px 20px;
    }
  }
  .div-4 {
    align-self: end;
    display: flex;
    width: 265px;
    max-width: 100%;
    align-items: end;
    justify-content: space-between;
    gap: 20px;
  }
  .div-5 {
    color: #fff;
    text-align: center;
    margin-top: 41px;
    flex: 1;
    font: 400 24px Inter, sans-serif;
  }
  @media (max-width: 991px) {
    .div-5 {
      margin-top: 40px;
    }
  }
  .div-6 {
    align-self: start;
    display: flex;
    align-items: end;
    gap: 12px;
  }
  .img {
    aspect-ratio: 0.95;
    object-fit: contain;
    object-position: center;
    width: 63px;
    overflow: hidden;
    margin-top: 37px;
    max-width: 100%;
  }
  .img-2 {
    aspect-ratio: 0.92;
    object-fit: contain;
    object-position: center;
    width: 37px;
    overflow: hidden;
    align-self: start;
    max-width: 100%;
  }
  .div-7 {
    color: #fff;
    text-align: center;
    border-radius: 20px;
    background-color: #5c5c5c;
    align-self: stretch;
    margin-top: 28px;
    align-items: center;
    padding: 17px 20px;
    font: 400 24px Inter, sans-serif;
  }
  .div-8 {
    color: #272727;
    text-align: center;
    white-space: nowrap;
    border-radius: 20px;
    background-color: #e1e1e1;
    align-self: stretch;
    margin-top: 41px;
    align-items: center;
    padding: 16px 20px;
    font: 400 24px Inter, sans-serif;
  }
  @media (max-width: 991px) {
    .div-8 {
      white-space: initial;
      margin-top: 40px;
    }
  }
  .div-9 {
    color: #fff;
    text-align: center;
    white-space: nowrap;
    border-radius: 20px;
    background-color: #5c5c5c;
    align-self: stretch;
    margin-top: 42px;
    align-items: center;
    padding: 17px 20px;
    font: 400 24px Inter, sans-serif;
  }
  @media (max-width: 991px) {
    .div-9 {
      white-space: initial;
      margin-top: 40px;
    }
  }
  .div-10 {
    color: #fff;
    text-align: center;
    border-radius: 20px;
    background-color: #5c5c5c;
    align-self: stretch;
    margin-top: 41px;
    align-items: center;
    padding: 17px 20px;
    font: 400 24px Inter, sans-serif;
  }
  @media (max-width: 991px) {
    .div-10 {
      margin-top: 40px;
    }
  }
  .div-11 {
    color: #fff;
    text-align: center;
    width: 240px;
    border-radius: 20px;
    background-color: #5c5c5c;
    align-self: stretch;
    align-items: center;
    margin: 42px 0 -87px;
    padding: 12px 20px;
    font: 400 24px Inter, sans-serif;
  }
  @media (max-width: 991px) {
    .div-11 {
      margin: 40px 0 10px;
    }
  }
  .column-2 {
    display: flex;
    flex-direction: column;
    line-height: normal;
    width: 75%;
    margin-left: 20px;
  }
  @media (max-width: 991px) {
    .column-2 {
      width: 100%;
    }
  }
  .div-12 {
    display: flex;
    margin-top: 6px;
    flex-direction: column;
  }
  @media (max-width: 991px) {
    .div-12 {
      max-width: 100%;
      margin-top: 13px;
    }
  }
  .div-13 {
    border-radius: 20px;
    background-color: #5c5c5c;
    display: flex;
    justify-content: space-between;
    gap: 20px;
    padding: 27px 476px 27px 27px;
  }
  @media (max-width: 991px) {
    .div-13 {
      max-width: 100%;
      flex-wrap: wrap;
      padding: 0 20px;
    }
  }
  .img-3 {
    aspect-ratio: 0.98;
    object-fit: contain;
    object-position: center;
    width: 42px;
    overflow: hidden;
    max-width: 100%;
  }
  .div-14 {
    color: #fff;
    text-align: center;
    margin: auto 0;
    font: 400 24px Inter, sans-serif;
  }
  .div-15 {
    border-radius: 20px;
    background-color: #5c5c5c;
    margin-top: 6px;
    padding: 26px 75px 50px;
  }
  @media (max-width: 991px) {
    .div-15 {
      max-width: 100%;
      padding: 0 20px;
    }
  }
  .div-16 {
    gap: 20px;
    display: flex;
  }
  @media (max-width: 991px) {
    .div-16 {
      flex-direction: column;
      align-items: stretch;
      gap: 0px;
    }
  }
  .div-17 {
    border-radius: 40px;
    background-color: #fff;
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: 0 auto;
    padding: 19px 16px 19px 25px;
  }
  @media (max-width: 991px) {
    .div-17 {
      margin-top: 40px;
      padding-left: 20px;
    }
  }
  .img-4 {
    aspect-ratio: 0.46;
    object-fit: contain;
    object-position: center;
    width: 115px;
    overflow: hidden;
  }
  .div-18 {
    color: #000;
    text-align: center;
    align-self: center;
    margin-top: 14px;
    white-space: nowrap;
    font: 400 24px Gluten, sans-serif;
  }
  @media (max-width: 991px) {
    .div-18 {
      white-space: initial;
    }
  }
  .column-3 {
    display: flex;
    flex-direction: column;
    line-height: normal;
    width: 25%;
    margin-left: 20px;
  }
  @media (max-width: 991px) {
    .column-3 {
      width: 100%;
    }
  }
  .div-19 {
    border-radius: 40px;
    background-color: #fff;
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: 0 auto;
    padding: 16px 16px 22px 25px;
  }
  @media (max-width: 991px) {
    .div-19 {
      margin-top: 40px;
      padding-left: 20px;
    }
  }
  .img-5 {
    aspect-ratio: 0.45;
    object-fit: contain;
    object-position: center;
    width: 115px;
    overflow: hidden;
  }
  .div-20 {
    color: #000;
    text-align: center;
    align-self: center;
    margin-top: 10px;
    white-space: nowrap;
    font: 400 24px Gluten, sans-serif;
  }
  @media (max-width: 991px) {
    .div-20 {
      white-space: initial;
    }
  }
  .column-4 {
    display: flex;
    flex-direction: column;
    line-height: normal;
    width: 25%;
    margin-left: 20px;
  }
  @media (max-width: 991px) {
    .column-4 {
      width: 100%;
    }
  }
  .div-21 {
    border-radius: 40px;
    background-color: #fff;
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: 0 auto;
    padding: 16px 16px 22px 25px;
  }
  @media (max-width: 991px) {
    .div-21 {
      margin-top: 40px;
      padding-left: 20px;
    }
  }
  .img-6 {
    aspect-ratio: 0.45;
    object-fit: contain;
    object-position: center;
    width: 115px;
    overflow: hidden;
  }
  .div-22 {
    color: #000;
    text-align: center;
    align-self: center;
    margin-top: 10px;
    white-space: nowrap;
    font: 400 24px Gluten, sans-serif;
  }
  @media (max-width: 991px) {
    .div-22 {
      white-space: initial;
    }
  }
  .column-5 {
    display: flex;
    flex-direction: column;
    line-height: normal;
    width: 25%;
    margin-left: 20px;
  }
  @media (max-width: 991px) {
    .column-5 {
      width: 100%;
    }
  }
  .div-23 {
    border-radius: 40px;
    background-color: #fff;
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: 5px auto 0;
    padding: 18px 15px 18px 26px;
  }
  @media (max-width: 991px) {
    .div-23 {
      margin-top: 40px;
      padding-left: 20px;
    }
  }
  .img-7 {
    aspect-ratio: 0.45;
    object-fit: contain;
    object-position: center;
    width: 115px;
    overflow: hidden;
  }
  .div-24 {
    color: #000;
    text-align: center;
    align-self: center;
    margin-top: 10px;
    white-space: nowrap;
    font: 400 24px Gluten, sans-serif;
  }
  @media (max-width: 991px) {
    .div-24 {
      white-space: initial;
    }
  }
  </style>