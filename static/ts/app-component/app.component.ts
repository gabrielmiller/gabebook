import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <h1>Hello {{test}}</h1>
    `
})

export class AppComponent {
  test = 'World';
}
