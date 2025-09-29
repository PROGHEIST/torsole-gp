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
  
}
