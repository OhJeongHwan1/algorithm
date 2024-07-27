// function sayHello() {
//   console.log(i);
//   for (var i = 0; i < 3; i++) {
//     setTimeout(() => {
//       console.log(i);
//     }, 1000 * i);
//   }
// }/
// sayHello();

const num = 0;

var Constructor = function (name) {
  this.name = name;
};

Constructor.prototype.method1 = function () {};
Constructor.prototype.property1 = "생성자 프로토타입 프로퍼티";

var instance = new Constructor("인스턴스");
console.dir(Constructor);
console.dir(instance);
