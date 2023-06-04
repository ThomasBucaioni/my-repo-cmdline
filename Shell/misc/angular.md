# Building and deploying and Angular app

## Install

```
node --version
npm --version
npm install -g @angular/cli@latest
ng --version
```

## New app

```
ng new angular-app
cd angular-app
ng serve --port $PORT --host $IP --disable-host-check
```

## Component

```
vim app.component.html
<router-outlet></router-outlet>

ng generate component first
vim tsconfig.json

vim app.component.html
<app-first></app-first>

ng generate component second
ng gererate component third

ng g c navigation

vim app.component.html
<app-navigation></app-navigation>
<ul>
    <li>First component</li>
    <li>Second component</li>
    <li>Third component</li>
</ul>

vim navigation.component.html
    public navigate(page: string) {
        this.router.navigate([page]>
    }

vim app-routing.module.ts
const routes: Routes = [
    { path: '', component: FirstComponent },
    { path: 'first', component: FirstComponent },
    { path: 'second', component: SecondComponent },
    { path: 'third', component: ThirdComponent },
    { path: '**', redirectTo: ''}
]
```

## Deployment

```
ng deploy
```


