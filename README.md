This project involves the development of a smart scale to monitor beverage stock in real-time, aimed at high-end bars. The system consists of an ESP32 connected to a camera for barcode reading and a scale for measuring the weight of the bottles.

Main functionalities:

    Barcode Reading: The camera, connected to the ESP32, reads the barcode of the bottle when it is placed on the scale.
    Weight Measurement: The scale measures the weight of the bottle and sends the data to the system.
    Data Update: The barcode and weight data are sent to a PostgreSQL database through a Python-based Rest API.
    Real-time Update: A website, developed with the Vue.Js framework, displays the updated weight value in real-time without the need for page refresh.

This system provides an efficient solution for high-end bars, allowing precise and real-time control of opened beverage stock, optimizing management and preventing losses.
