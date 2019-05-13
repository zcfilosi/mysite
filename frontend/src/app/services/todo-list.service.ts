import { Injectable } from '@angular/core';
import { HttpClient} from  '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TodoListService {

  constructor(private  httpClient:  HttpClient) { }
  getFirstPage(){
    return  this.httpClient.get('${this.API_URL}/todoList');
  }
}
