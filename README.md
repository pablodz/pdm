# MedicPUCP - Web

[![Build Status](https://travis-ci.com/ZurMaD/pdm.svg?branch=master)](https://travis-ci.com/ZurMaD/pdm)


<br />
<p align="center">
  <a href="#">
    <img src="/docs/img/logo.png">
  </a>

  <h3 align="center">Web MedicPUCP <br>
  Vital signs management system of health centers</h3>

  <p align="center">
    <br />
    <a href="https://pdm3.herokuapp.com">View Demo</a>
    ·
    <a href="#">Report Bug</a>
    ·
    <a href="#">Request Feature</a>
  </p>
</p>
<hr style="height:2px;border-width:0;color:gray;background-color:gray">


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [What is MedicPUCP?](#what-is)
* [How it works?](#how-works)
* [Our users can:](#our-users)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [General updates](#general-updates)


<!-- ABOUT THE PROJECT -->
## About The Project

[Content]

<!-- What is MedicPUCP? -->
## What is MedicPUCP?

Our platform is responsible for collecting and processing data from associated devices (MedicKit & MedicBand) from each associated health personnel of a certain health center. Our servers are in charge of processing data and converting it into metrics in order to make decisions, in addition to real-time monitoring of all associated sensors.

We provide platforms for administrative personnel and their associates to access from anywhere in the world.

<!-- How it works? -->
## How it works?

[Content]

<!-- Our users can: -->
## Our users can:

- `If is an administrative`: `[Content]`
- `If is a normal user`: `[Content]`
- `If is a mantainer`: `[Content]`

<!-- ROADMAP -->
## Roadmap

See the [open issues](#) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- General system updates -->
## General updates

System: Web ([Heroku](https://www.github.com/zurmad/pdm)) + Web (Grafana - Not public yet) + App ([Flutter](https://www.github.com/zurmad/pdm-app))

### 2020-07-13 (Spanish for now)
- [x] Asignar kid_id a usuarios. (Se creo tabla para manejar asociación - No automático)
- [x] Enviar valores de batería. (Se tiene tabla que registra los valores)
- [x] Enviar alertas al administrador.
- [x] WEB: Cambiar variables a nombres, apellidos y DNI.
- [x] WEB: Quitar pestañas anteriores que son irrelevantes o no aportan el valor deseado.
- [x] APP: Añadir notificaciones de grafana
- [x] WEB: Tener historial de alertas.
- [x] WEB: Personas con presión arterial, frecuencia respiratoria o temperatura corporal anómala.
- [x] GRAFANA: Agregar batería al dashboard
- [x] APP: Cambiar fondos de imagenes con emoticones en el texto.
- [x] APP: Tener historial de alertas.
- [x] APP: Cambiar tiempos de muestreo por lista según app.
- [x] APP: Añadir loader mientras carga login token.
- [] APP: Refresh automático de valores.
- [] APP: Cambiar colores cuando estén o no dentro del rango saludable. (Sin API para no complicar)

### 2020-06-10

- [x] Find fast framework to develop in 
- [x] Fork an app to to an app
- [x] Find a graph system
- [x] Create graph system that alerts with webhooks.
- [x] Find the best database: Postgres with Timescale selected.
- [x] Create architecture for IoT lowcost.