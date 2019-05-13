import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { MatInputModule, MatButtonModule, MatCardModule, MatFormFieldModule,MatTableModule } from  '@angular/material';
import { Routes, RouterModule } from '@angular/router';
import { HttpClientModule } from  '@angular/common/http';

import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { TodoListComponent } from './todo-list/todo-list.component';
import { TodoCreateComponent } from './todo-create/todo-create.component';
import { TodoDeleteComponent } from './todo-delete/todo-delete.component';

const appRoutes: Routes = [
  { path: '', redirectTo: 'todoList', pathMatch: 'full' },
  {
    path: 'todoList',
    component: TodoListComponent
  },
  {
    path: 'createToDo',
    component: TodoCreateComponent
  },
  {
    path: 'deleteToDo',
    component: TodoDeleteComponent
  }
];


@NgModule({
  declarations: [
    AppComponent,
    TodoListComponent,
    TodoCreateComponent,
    TodoDeleteComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    MatTableModule,
    MatCardModule,
    MatInputModule,
    MatFormFieldModule,
    MatButtonModule,
    RouterModule.forRoot(
      appRoutes,
      { enableTracing: true } // <-- debugging purposes only
    )
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
