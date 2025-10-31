# TODO: Remove Population Chart from Village Population Component

- [x] Edit src/app/components/village-population/village-population.html to remove the chart section (the div containing the canvas and related elements)
- [x] Edit src/app/components/village-population/village-population.ts to remove Chart.js imports, chart property, createChart method, and ngAfterViewInit method
- [x] Check if Chart.js is used elsewhere in the project; if not, remove it from package.json
- [ ] Run the app to verify the component displays stats and table without the chart
