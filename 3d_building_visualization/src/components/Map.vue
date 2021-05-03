<template>
  <div class="row-start-1">
    <div id="mapContainer"></div>
    <div id="staticMap"></div>
  </div>
</template>

<script setup>
</script>

<script>
import "mapbox-gl/dist/mapbox-gl.css";
import mapboxgl from "mapbox-gl/dist/mapbox-gl";
import THREE from "three/build/three";

export default {
  name: "Map",
  data() {
    return {
      lat: 43.00088772365117,
      lon: -78.78900188413338,
      zoom: 15.5,
      accessToken:
        "pk.eyJ1Ijoid2FuZzE5ODkxMjE4IiwiYSI6ImNrbzV5cW00ZTB2aDkybnF3YzViZm53eWcifQ.WT6W87ykSXJD8Wp63wm-yQ",
    };
  },
  methods: {
    setupMap: function () {
      mapboxgl.accessToken = this.accessToken;

      var map = new mapboxgl.Map({
        style: "mapbox://styles/mapbox/light-v10",
        // style: 'mapbox://styles/mapbox/streets-v11',
        center: [this.lon, this.lat],
        zoom: this.zoom,
        pitch: 45,
        bearing: 0,
        container: "mapContainer",
        antialias: true,
      });

      map.on("load", function () {
        // Insert the layer beneath any symbol layer.
        var layers = map.getStyle().layers;
        var labelLayerId;
        for (var i = 0; i < layers.length; i++) {
          if (layers[i].type === "symbol" && layers[i].layout["text-field"]) {
            labelLayerId = layers[i].id;
            break;
          }
        }
        // The 'building' layer in the Mapbox Streets
        // vector tileset contains building height data
        // from OpenStreetMap.
        map.addLayer({
          id: "add-3d-buildings",
          source: "composite",
          "source-layer": "building",
          filter: ["==", "extrude", "true"],
          type: "fill-extrusion",
          minzoom: 15,
          paint: {
            "fill-extrusion-color": "#aaa",
            // Use an 'interpolate' expression to
            // add a smooth transition effect to
            // the buildings as the user zooms in.
            "fill-extrusion-height": [
              "interpolate",
              ["linear"],
              ["zoom"],
              15,
              0,
              15.05,
              ["get", "height"],
            ],
            "fill-extrusion-base": [
              "interpolate",
              ["linear"],
              ["zoom"],
              15,
              0,
              15.05,
              ["get", "min_height"],
            ],
            "fill-extrusion-opacity": 0.6,
          },
        });
      });
    },
  },
  mounted() {
    this.setupMap();
  },
};
</script>

<style>
#mapContainer {
  min-width: 400px;
  width: 100%;
  max-width: 800px;
  min-height: 300px;
  height: 450px;
  max-height: 600px;
}
#staticMap {
  width: 100%;
  height: 100%;
  grid-column: 1;
  grid-row: 1;
}
</style>
