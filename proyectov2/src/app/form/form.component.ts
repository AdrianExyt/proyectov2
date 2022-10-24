import { Component, OnInit } from '@angular/core';
import data from '../../assets/countries.json';

interface COUNTRY {
  name_en: string;  
  name_es: string;
}

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent implements OnInit {

  Countries: COUNTRY[] = data;

  postUserFormData(formData:any){
    console.warn(formData);
  }

  constructor() { }

  ngOnInit(): void {

  }

}
