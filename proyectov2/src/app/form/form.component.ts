import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import data from '../../assets/countries.json';

interface COUNTRY {
  name_en: string;  
  name_es: string;
}
class ImageSnippet {
  constructor(public src: string, public file: File) {}
}

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent implements OnInit {

  Countries: COUNTRY[] = data;
  

  postUserFormData(formData: {textInputName: string, textInputSurname: string, emailInput: string, passwordInput: string, countryInput: string, imgStored: boolean}, event: any){
    console.warn(formData);
    let fileLista: File = event.target[5].files[0];
    console.warn(fileLista);
    if(fileLista){
      formData.imgStored = true;
    } else {
      formData.imgStored = false;
    }

    const formDataJson = JSON.stringify(formData)

    this.http.post("http://127.0.0.1:8000/form", formDataJson).subscribe((res) => {
      console.log(res);
    });

    this.sendFileData(fileLista)
  }

  sendFileData(file: File){
    
    if(file) {
      console.log(file);
      const formData = new FormData();
      formData.append("thumbnail", file);
        
        //let formData:FormData = new FormData();
        //formData.append('uploadFile', file, file.name);
        //let headers = new Headers();
        //headers.append('Content-Type', 'multipart/form-data');
        //headers.append('Accept', 'application/json');
        
        this.http.post("http://127.0.0.1:8000/img", formData).subscribe((res) => {
          console.log(res);
        })
    }
    
  }

  constructor(private http: HttpClient) { 

  }

  ngOnInit(): void {

  }

}
