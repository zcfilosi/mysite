import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HttpModule } from '@angular/http';

import { ShowDataComponent } from './show-data/show-data.component';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';

import { AppRoutingModule } from "./app.router";

import { AppComponent } from './app.component';


@NgModule({
  declarations: [
    AppComponent,
    ShowDataComponent,
    PagenotfoundComponent

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpModule

  ],

  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
