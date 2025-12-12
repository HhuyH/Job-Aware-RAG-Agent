---
title: Model Checkpointing in Deep Learning
description: Ghi chú về kỹ thuật Model Checkpointing trong deep learning, mục đích lưu trạng thái mô hình, cách thực hiện và ứng dụng thực tế.
tags: [Deep Learning, Training, Model Checkpointing, Saving Models, Optimization]
---

## 1. Tóm tắt khái niệm (Definition)

Model checkpointing là quá trình lưu trạng thái mô hình (weights, optimizer state) trong quá trình training để có thể khôi phục hoặc tiếp tục training sau này.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Phòng tránh mất training do sự cố.
* Lưu mô hình tốt nhất theo validation loss/accuracy.
* Tiếp tục training từ checkpoint thay vì train lại từ đầu.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* Sau mỗi epoch hoặc khi điều kiện thỏa, lưu:
  $$
  M_{checkpoint} = {\theta, \eta, optimizer_state}
  $$
* `theta`: trọng số mô hình, `eta`: learning rate, `optimizer_state`: trạng thái optimizer.
* Khi load checkpoint, mô hình và optimizer khôi phục trạng thái, training tiếp tục chính xác như trước.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

* Save:
  $$
  \text{save_checkpoint}(model, optimizer, epoch, path)
  $$
* Load:
  $$
  model, optimizer = \text{load_checkpoint}(path)
  $$
* Kiểm soát lưu best model theo metric:
  $$
  \text{if validation_loss < best_loss: save_checkpoint(...)}
  $$

---

## 5. Ví dụ code (Code Examples)

```python
import torch

# Save checkpoint
def save_checkpoint(model, optimizer, epoch, path):
    torch.save({
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict()
    }, path)

# Load checkpoint
def load_checkpoint(model, optimizer, path):
    checkpoint = torch.load(path)
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    return model, optimizer, checkpoint['epoch']

# Example usage
model, optimizer, start_epoch = load_checkpoint(model, optimizer, 'checkpoint.pth')
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Không lưu optimizer state → learning rate và momentum không khôi phục.
* Lưu checkpoint quá thường xuyên → tốn storage.
* Không lưu best model theo validation metric → load lại mô hình chưa tốt nhất.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* Checkpointing vs Regular Saving:

  * Checkpointing: lưu trạng thái có thể resume training.
  * Regular save: lưu weights cuối cùng, không chắc resume được.
* Checkpointing vs Early Stopping:

  * Early stopping dừng training sớm.
  * Checkpointing lưu trạng thái tốt nhất trong quá trình training.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Training deep network lớn tốn nhiều thời gian → checkpointing bắt buộc.
* Kết hợp với early stopping để lưu best model.
* Distributed training: mỗi node có checkpoint riêng, tổng hợp khi cần.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Model checkpointing là gì và tại sao cần?
* Khi nào nên lưu checkpoint?
* Có gì cần lưu ngoài weights?
* Checkpointing kết hợp với early stopping như thế nào?

---

## 10. TL;DR (Short Summary)

* Checkpointing: lưu trạng thái mô hình và optimizer.
* Giúp resume training, lưu best model.
* Lưu sau mỗi epoch hoặc khi validation loss cải thiện.
* Kết hợp với early stopping và distributed training.
