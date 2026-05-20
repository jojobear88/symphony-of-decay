# KỊCH BẢN GAME VISUAL NOVEL: BẢN GIAO HƯỞNG CỦA SỰ MỤC RỮA
# KHỞI ĐẦU BẢN DEMO - NGÀY THỨ 31

# -------------------------------------------------------------------------
# 1. KHAI BÁO NHÂN VẬT VÀ MÀU SẮC TÊN
# -------------------------------------------------------------------------
define az = Character("An Thái", color="#ff6f00")       # Xám - u tối, nhẫn nhịn
define lp = Character("Lê Phi", color="#c2a200")       # Xanh dương - bộc trực, lạnh lùng dần
define fl = Character("Phương Linh", color="#FF69B4") # Hồng cánh sen - hoàn hảo, điên loạn ngầm
define cc = Character("Chu Cường", color="#808080")  # Đỏ - biến động, bạo lực
define zb = Character("Trí Ba", color="#00028b")       # Đỏ thẫm - kẻ bắt nạt
define sys = Character("HỆ THỐNG", color="#502427")     # Xanh lá - thông báo máy móc

# -------------------------------------------------------------------------
# 2. KHỞI TẠO HỆ THỐNG CHỈ SỐ (VARIABLES)
# -------------------------------------------------------------------------
default food_count = 2          # Số lượng thịt hộp còn lại
default barricade_level = 1     # Cấp độ phòng thủ của phòng nhạc (1-5)

# Chỉ số sinh tồn của từng nhân vật (Thang điểm 100)
default az_hp = 70
default az_sanity = 65

default lp_hp = 80
default lp_sanity = 70

default fl_hp = 65
default fl_sanity = 50          # Fang Ling có mức tỉnh táo thấp sẵn do áp lực

default cc_hp = 90
default cc_sanity = 60

# -------------------------------------------------------------------------
# 3. BẮT ĐẦU GAMEPLAY
# -------------------------------------------------------------------------
label start:
    camera:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.2)*SaturationMatrix(0.5)
    
    scene bg music_room_morning with fade
    # play music "audio/ambient_creepy_drone.ogg" loop

    sys "NGÀY THỨ 31. BẮT ĐẦU GIAI ĐOẠN THỬ NGHIỆM: 'SỰ KHAN HIẾM'."
    sys "Kể từ ngày hôm nay, nguồn cung cấp lương thực định kỳ sẽ bị CẮT GIẢM vô thời hạn."

    az "(Hôm nay... tiếng xe đẩy tiếp tế của bọn chúng không vang lên ngoài hành lang nữa.)"
    az "(Đã quá giờ hẹn ba tiếng đồng hồ. Cái dạ dày của tôi bắt đầu cào xé, nhắc nhở về một thực tế tồi tệ.)"

    # Hiển thị nhân vật Li Pei (Dùng hình ảnh tạm thời của bạn nếu có)
    # show sprite_li_pei_anxious at left
    lp "Thái này... Cậu nghe thấy không? Tiếng loa phát thanh vừa tắt đấy."
    lp "Tớ đã kiểm tra hòm thư ở cửa rồi. Trống rỗng. Không có lấy một mẩu bánh mì vụn."

    # show sprite_fang_ling_forced_smile at right
    fl "Đừng làm ầm lên thế, Phi. Thật vô giáo dục."
    fl "Cha chị nói, trong mọi nghịch cảnh, người có học thức phải giữ được sự điềm tĩnh."

    az "Chị Linh, ngón tay chị... đang chảy máu kìa."

    # Miêu tả hành động tâm lý
    "Phương Linh giật mình, nhìn xuống mười đầu ngón tay đang miết chặt vào những phím đàn Organ vỡ nát. Cô đã cạo nó đến mức bật máu để tìm kiếm sự tỉnh táo."
    
    fl "Ồ... chị không đau. Chỉ là một chút bụi bẩn thôi. Chị phải lau sạch nó."
    $ fl_sanity -= 5  # Giảm chỉ số tỉnh táo của Fang Ling

    # show sprite_chu_cang_depressed at center
    cc "Chúng ta sẽ chết đói... Chúng ta sẽ giống như mấy đứa ở câu lạc bộ vẽ... bị chúng nó mang đi làm xác mổ..."
    cc "Tôi không muốn chết! Tôi muốn về nhà!"

    menu:
        az "(Anh Cường lại bắt đầu mất kiểm soát rồi. Mình phải làm gì đây?)"
        
        "An ủi anh Chu Cường (Tăng độ tỉnh táo cho Chu Cường)":
            $ cc_sanity += 10
            az "Bình tĩnh lại đi anh Cường. Chúng ta vẫn còn hai hộp thịt dự trữ. Chúng ta sẽ ổn thôi."
            cc "Thật... thật không An Thái? Em không lừa anh chứ?"
            az "Em không lừa anh. Nhưng chúng ta phải tiết kiệm."

        "Đe dọa để anh ta im lặng (Giảm tỉnh táo, giữ nhịp độ lạnh lùng)":
            $ cc_sanity -= 10
            $ az_sanity -= 5
            az "Câm mồm vào đi anh Cường! Anh muốn tiếng khóc của anh dụ bọn Trí Ba hoặc lũ khủng bố đến đây à?"
            az "Muốn chết thì biến ra ngoài hành lang mà chết!"
            "Chu Cường run bắn người, co rúm lại vào góc tối, ôm khư khư cây Cello gãy dây."

# -------------------------------------------------------------------------
# 4. VÒNG LẶP BAN NGÀY (CRAFTING / NGHỈ NGƠI)
# -------------------------------------------------------------------------
label daytime_loop:
    scene bg_music_room_day with fade
    az "(Bây giờ là ban ngày. Chúng ta tạm thời an toàn trong căn phòng này, nhưng không thể ngồi im chờ chết.)"

    menu:
        az "Mình nên làm gì vào lúc này?"

        "Kiểm tra kho lương thực":
            sys "Số lượng thịt hộp hiện tại: [food_count] hộp."
            if food_count > 0:
                menu:
                    "Phân chia 1 hộp thịt cho cả nhóm (Tăng HP, giảm đói)":
                        $ food_count -= 1
                        $ az_hp += 10
                        $ lp_hp += 10
                        $ fl_hp += 10
                        $ cc_hp += 10
                        az "Mỗi người một thìa. Ăn chậm thôi, đừng để bị nôn."
                    "Tiếp tục nhịn ăn để tích trữ":
                        az "Chúng ta phải nhịn thêm hôm nay. Chưa đến mức phải mở hộp thịt cuối cùng."
                        $ az_hp -= 5
                        $ lp_hp -= 5
            jump daytime_loop

        "Gia cố phòng nhạc (Chế tạo)":
            az "(Cửa chính hơi lỏng lẻo. Mình có thể bảo Li Pei dùng ván gỗ đập vỡ từ ghế để đóng chặt nó lại.)"
            $ barricade_level += 1
            $ lp_hp -= 10
            sys "Phòng nhạc đã được gia cố. Cấp độ phòng thủ hiện tại: [barricade_level]/5."
            lp "Xong rồi đấy. Thằng chó nào muốn phá cửa này ban đêm sẽ phải tốn kha khá sức đấy."
            jump daytime_loop

        "Kết thúc ban ngày, chuẩn bị cho ban đêm":
            jump nighttime_start

# -------------------------------------------------------------------------
# 5. VÒNG LẶP BAN ĐÊM (EXPLORATION / NIGHTTIME)
# -------------------------------------------------------------------------
label nighttime_start:
    scene bg_corridor_dark with flash
    play music "audio/heartbeat_and_wind.ogg" loop
    
    az "(Màn đêm buông xuống. Thành phố Henei ngoài kia lên đèn, nhưng hành lang này là một cái bẫy chết người.)"
    az "(Chúng ta không thể nhịn đói mãi. Phải cử người đi tìm thêm đồ ăn.)"

    menu:
        az "Ai sẽ ra ngoài đêm nay, và ai sẽ ở lại thủ nhà?"

        "Ah Zai đi săn cùng Li Pei (Đội hình tấn công nhanh)":
            az "Li Pei, cầm lấy dùi trống. Đi với tớ sang khu Căng tin."
            lp "Được, tớ sẵn sàng rồi. Để anh Cang và chị Ling ở lại giữ phòng."
            jump event_encounter_zhiba

        "Cử anh Chu Cang đi một mình (Rủi ro cao, sức mạnh lớn)":
            if cc_sanity < 40:
                az "Anh Cang, tâm trạng anh đang bất ổn, ra ngoài băm nát đứa nào cản đường đi."
                cc "(Gầm gừ) Giết... tôi sẽ giết hết tụi nó..."
                jump event_encounter_zhiba
            else:
                az "Anh Cang khỏe nhất, anh đi thám hiểm phòng Y tế xem có băng gạc không nhé."
                jump event_encounter_zhiba

# -------------------------------------------------------------------------
# 6. KỊCH BẢN SỰ KIỆN: ĐỤNG ĐỘ ZHI BA (EVENT)
# -------------------------------------------------------------------------
label event_encounter_zhiba:
    scene bg_canteen_destroyed with fade
    "Ah Zai và Li Pei lướt đi trong bóng tối của dãy hành lang khối B. Mùi rác thải và mùi máu xộc lên mũi."
    "Đột nhiên, một ánh đèn pin rọi thẳng vào mặt hai người."

    zb "Ồ, xem ai đây? Lũ chuột nhắt của câu lạc bộ âm nhạc."
    zb "Thằng lùn Ah Zai, bố mẹ mày làm lao công quét rác thì chắc mày giỏi bới rác tìm đồ ăn lắm nhỉ? Giao hết đồ nhặt được ra đây!"

    menu:
        zb "Mày chọn đi: Bị tao bẻ gãy tay, hay để lại đồ ăn?"

        "Đàm phán và bỏ chạy (Giữ an toàn, mất tài nguyên)":
            az "Chúng tôi không có đồ ăn! Cầm lấy đống sắt vụn này đi và để chúng tôi yên!"
            "Zhi Ba giật lấy túi sắt vụn, nhổ một bãi nước bọt vào mặt Ah Zai rồi bỏ đi."
            $ az_sanity -= 10
            jump day_end

        "Ra lệnh cho Li Pei tấn công (Kích hoạt bạo lực)":
            az "Li Pei... b bịt mồm nó lại. Không được để nó hét lên."
            
            # Đoạn văn mô tả Gore (Máu me) đúng chất Light Novel
            "Không một lời phản kháng, Li Pei lao lên như một mũi tên. Đôi dùi trống bằng gỗ sồi vát nhọn đâm thẳng vào bắp đùi của Zhi Ba."
            zb "Áaaaa! Thằng chó... cứu—"
            "Ah Zai lập tức lao tới, dùng phần loa kèn Trumpet kim loại nện thẳng vào miệng Zhi Ba, biến tiếng hét của hắn thành những tiếng ngụm máu nghẹn ngào."
            
            $ lp_sanity -= 10
            $ az_sanity -= 5
            sys "Bạn đã đánh bại Zhi Ba. Hắn bị thương nặng và bị kéo về phòng nhạc làm tù binh."
            jump day_end

label day_end:
    sys "KẾT THÚC NGÀY THỨ 31. Chỉ số hiện tại đã được cập nhật."
    # Đoạn này sẽ hiển thị màn hình chúc mừng hoặc chuyển sang Ngày 32
    return