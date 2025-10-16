# Examinerande Uppgift: Maskininlärningsprojekt från Data till Web-API
##  Datainsamling och Urval
### Valt dataset
Jag har valt Breast Cancer Wisconsin (Diagnostic) Dataset, som finns publikt tillgängligt på Kaggle . Datasetet härstammar ursprungligen från UCI Machine Learning Repository, som är en välkänd källa för öppna dataset inom maskininlärning.
### Beskrivning av datasetet
Datasetet innehåller information från 569 patienter med totalt 30 olika mätvariabler relaterade till cellkärnornas egenskaper i bröstvävnadsprover. Variablerna är bland annat:

Radius, Texture, Perimeter, Area, Smoothness, Compactness, Concavity, med flera. Varje observation representerar ett tumörprov och varje rad är märkt med en av två klasser:
 - Malignant (elakartad)
 - Benign (godartad)

### Motivering till valet
Jag valde detta dataset eftersom:
- Datasetet är balanserat och tydligt, vilket passar bra för att träna och utvärdera olika klassifikationsmodeller.
- Variablerna är numeriska , vilket underlättar för analys och modellering.

### Prediktionsuppgift
Den specifika uppgiften är att klassificera om en tumör är elakartad eller godartad baserat på de diagnostiska mätvärdena. Detta är en binär klassifikationsuppgift, där målet är att bygga en modell som kan förutsäga cancertypen utifrån insamlade medicinska data.

## Access the API:

The REST API endpoints are available at:

```bash
http://localhost:5000/predict

And json post format like this :

{
  "features":
      [10.420,20.38, 77.58,386.1,0.14250, 0.28390,0.241400, 0.105200, 0.2597, 0.09744, 0.4956,1.1560,3.4450,27.230,0.009110,0.074580,0.056610,0.018670,0.059630,0.009208,14.910,26.50,98.87,567.7,0.20980,0.86630,0.686900,0.257500,0.6638,0.17300]
}
```
