import { Component, AfterViewInit } from '@angular/core';
import * as L from 'leaflet';

@Component({
  selector: 'app-map-location',
  standalone: false,
  templateUrl: './map-location.html',
  styleUrl: './map-location.css'
})
export class MapLocation implements AfterViewInit {
  private map: L.Map | undefined;

  ngAfterViewInit(): void {
    this.initMap();
  }

  private initMap(): void {
    // Coordinates for the location
    const lat = 16.3444;
    const lng = 73.5521;

    // Create the map centered at the given location
    this.map = L.map('map', {
      center: [lat, lng],
      zoom: 15,
      maxBounds: [
        [lat - 0.002, lng - 0.002], // Southwest corner (very tight bounds)
        [lat + 0.002, lng + 0.002]  // Northeast corner
      ],
      maxBoundsViscosity: 1.0, // Prevents dragging outside bounds
      inertia: false, // Disable inertia to reduce flickering on scroll
      scrollWheelZoom: false, // Disable zoom on scroll to prevent flickering
      dragging: true,
      touchZoom: false,
      doubleClickZoom: false,
      boxZoom: false,
      keyboard: false
    });

    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: ''
    }).addTo(this.map);

    // Add a marker at the location
    L.marker([lat, lng]).addTo(this.map)
      .bindPopup('<b>तोरसोळे</b><br>Location: 16.3444° N, 73.5521° E')
      .openPopup();

    // Fit the map to the bounds to ensure it stays within the restricted area
    this.map.fitBounds([
      [lat - 0.002, lng - 0.002],
      [lat + 0.002, lng + 0.002]
    ]);

    // Invalidate size to fix potential flickering issues
    setTimeout(() => {
      this.map?.invalidateSize();
    }, 100);
  }
}
