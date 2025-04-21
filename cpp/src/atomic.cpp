#include <atomic>
#include <iostream>
#include <thread>

std::atomic<int> turn(0);

void printA(int count) {
  for (int i = 0; i < count; i++) {
    while (turn != 0) {
    }
    std::cout << "A" << std::endl;
    turn = 1;
  }
}
void printB(int count) {
  for (int i = 0; i < count; i++) {
    while (turn != 1) {
    }
    std::cout << "B" << std::endl;
    turn = 2;
  }
}
void printC(int count) {
  for (int i = 0; i < count; i++) {
    while (turn != 2) {
    }
    std::cout << "C" << std::endl;
    turn = 0;
  }
}
int main(int argc, const char **argv) {
  int count = 3;
  std::thread a(printA, count);
  std::thread b(printB, count);
  std::thread c(printC, count);
  a.join();
  b.join();
  c.join();

  return 0;
}