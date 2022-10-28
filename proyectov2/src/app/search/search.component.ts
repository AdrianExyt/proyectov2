import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})

export class SearchComponent implements OnInit {
  
  constructor(private http: HttpClient) { }
  myData: any
  myData$: any

  getData(){
    this.http.get('http://localhost:8000/query').subscribe((res) => {
      this.myData = res;
      this.myData$ = this.myData
      console.log(this.myData);
    });
    return this.myData;
  }

  getFilterData(formData: {textFilter: string}){
    console.log(formData.textFilter);
    this.http.get('http://localhost:8000/query/'+formData.textFilter).subscribe((res) => {
      this.myData = res;
      this.myData$ = this.myData
      console.log(this.myData);
    });
    return this.myData;
  }

  downloadFile(fileDownload: any){

  }

  ngOnInit(): void {
    this.getData();
  }

}
