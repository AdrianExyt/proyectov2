import { Component } from '@angular/core';
import data from '../assets/countries.json';

interface COUNTRY {
  name_en: string;  
  name_es: string;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'proyectov2';

  Countries: COUNTRY[] = data;

  constructor(){
    console.log(this.Countries);
  }
}
