# World-Time-Device

The World Time Device is an intuitive display that showcases the local time of 9 major cities across the globe. Live data of the local time for each city is sourced from WorldTimeAPI (https://worldtimeapi.org).

---

### Functionality
The LCD Display in the map will show the current city selected and the local time at that city. The LED light corresponding to the selected city will also be lit on the map. Once the button on the map is pressed, the LCD Display will display the next city and its local time. The previously lit LED light will turn off, and the LED light corresponding to the next city will light up. Once the user has cycled through all the cities, the device will make a request to WorldTimeAPI to retrieve local time data for each city.

