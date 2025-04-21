#include <iostream>
#include <mutex>
#include <thread>
class ABC {
public:
  ABC(int count) : count_(count) {}
  void printA() {
    for (int i = 0; i < count_; i++) {
      std::unique_lock<std::mutex> lock(mtx_);
      cv_.wait(lock, [this] { return turn_ == 0; });
      std::cout << "A" << std::endl;
      turn_ = 1;
      cv_.notify_all();
    }
  }
  void printB() {
    for (int i = 0; i < count_; i++) {
      std::unique_lock<std::mutex> lock(mtx_);
      cv_.wait(lock, [this] { return turn_ == 1; });
      std::cout << "B" << std::endl;
      turn_ = 2;
      cv_.notify_all();
    }
  }
  void printC() {
    for (int i = 0; i < count_; i++) {
      std::unique_lock<std::mutex> lock(mtx_);
      cv_.wait(lock, [this] { return turn_ == 2; });
      std::cout << "C" << std::endl;
      turn_ = 0;
      cv_.notify_all();
    }
  }

private:
  std::mutex mtx_;
  std::condition_variable cv_;
  int count_;
  int turn_ = 0;
};

int main(int argc, const char **argv) {
  ABC abc(3);
  std::thread a(&ABC::printA, &abc);
  std::thread b(&ABC::printB, &abc);
  std::thread c(&ABC::printC, &abc);
  a.join();
  b.join();
  c.join();

  return 0;
}