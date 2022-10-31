import { Component, OnInit } from '@angular/core';
import countries_data from '../../assets/countries.json';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { HttpClient, HttpHeaders } from '@angular/common/http';

interface COUNTRY {
  name_en: string;  
  name_es: string;
}

@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.css']
})


export class EditComponent implements OnInit {
  Countries: COUNTRY[] = countries_data;
  User_data: any;
  user_id: string = "TEST";
  myData: any;

  constructor(private route: ActivatedRoute, private http: HttpClient) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.user_id = String(params['id']);
    })
    this.getUserData(this.user_id);
  }

  editUserFormData(formData: {textInputName: string, textInputSurname: string, emailInput: string, passwordInput: string, countryInput: string}){
    console.warn(formData);
    const formDataJson = JSON.stringify(formData)

    this.http.put("http://127.0.0.1:8000/edit/"+this.user_id, formDataJson).subscribe((res) => {
      console.log(res);
    });
  }

  getUserData(id: any){

    this.http.get('http://localhost:8000/edit/'+id).subscribe((res) => {
      this.User_data = res;
      console.log("AAAAAAAAAAAAAAAAAAA");
      console.log(this.User_data);
    });
  }
}