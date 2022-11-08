import http from 'k6/http';

export let options = {
  stages: [
      { duration: '600s', target: 10 },
      { duration: '600s', target: 3 },
      { duration: '600s', target: 1 },
  ],
};

export default function () {
  http.get('http://localhost:8080/login');
  http.get('http://localhost:8080/account');
  http.get('http://localhost:8080/payment');
}
