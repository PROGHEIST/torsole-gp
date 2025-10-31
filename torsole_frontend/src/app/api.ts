import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class Api {

  public apiUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) {}

  getAppData(): Observable<any>{
    return this.http.get<any>(`${this.apiUrl}/gpinfo`);
  }

  getCarosoulData(): Observable<any>{
    return this.http.get<any>(`${this.apiUrl}/slideshow`);
  }

  getAboutVillageData(): Observable<any>{
    return this.http.get<any>(`${this.apiUrl}/about-village`);
  }

  getMissionsData(): Observable<any>{
    return this.http.get<any>(`${this.apiUrl}/mission-objectives`);
  }

  getImpLinksData(): Observable<any>{
    return this.http.get<any>(`${this.apiUrl}/important-links`)
  }

  getGovernmentGrData(): Observable<any>{
    return this.http.get<any>(`${this.apiUrl}/goverment-grs`)
  }

  getGRDepartmentData(): Observable<any>{
    return this.http.get<any>(`${this.apiUrl}/gr-departments`)
  }
  
  getGPDocumentsData(): Observable<any>{
    return this.http.get<any>(`${this.apiUrl}/gp-documents`)
  }

  getPhotoGalleryData(): Observable<any>{
    return this.http.get<any>(`${this.apiUrl}/photo-gallery`)
  }

  getGPBodiesData(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/grampanchayat-bodies`)
  }

  getMahaOfficersData(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/maharastra-officers`)
  }

  getVillagePopulationData(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/torsole-village-population`)
  }

}
