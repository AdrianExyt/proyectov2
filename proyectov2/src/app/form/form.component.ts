import { HttpClient } from '@angular/common/http';
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

  postUserFormData(formData: {textInputName: string, textInputSurname: string, emailInput: string, passwordInput: string, countryInput: string}){
    console.warn(formData);

    const formDataJson = JSON.stringify(formData)

    this.http.post("http://127.0.0.1:8000/form", formDataJson).subscribe((res) => {
      console.log(res);
    });
  }

  constructor(private http: HttpClient) { 

  }

  ngOnInit(): void {

  }

}
