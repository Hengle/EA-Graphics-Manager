from inc_noesis import *
import struct

# EA Graphics Manager Noesis script
# Created by Bartlomiej Duda (Ikskoks)
# License: GPL-3.0 License
# This script is a part of the "EA Graphics Manager"
# More info here: https://github.com/bartlomiejduda/EA-Graphics-Manager


# This script is still in development.
# It may have some bugs. Some image types may be not supported.

SCRIPT_VERSION = "0.0.3"
SCRIPT_LAST_UPDATE = "11.05.2022"


debug_mode_enabled = True
is_image_twiddled = False


def registerNoesisTypes():
    handle = noesis.register("EA SSH (PS2) FILES", ".ssh")
    noesis.setHandlerTypeCheck(handle, ea_image_check_type)
    noesis.setHandlerLoadRGBA(handle, ea_image_load)

    handle = noesis.register("EA XSH (XBOX) FILES", ".xsh")
    noesis.setHandlerTypeCheck(handle, ea_image_check_type)
    noesis.setHandlerLoadRGBA(handle, ea_image_load)

    handle = noesis.register("EA MSH (PSP) FILES", ".msh")
    noesis.setHandlerTypeCheck(handle, ea_image_check_type)
    noesis.setHandlerLoadRGBA(handle, ea_image_load)

    handle = noesis.register("EA FSH (PC) FILES", ".fsh")
    noesis.setHandlerTypeCheck(handle, ea_image_check_type)
    noesis.setHandlerLoadRGBA(handle, ea_image_load)

    handle = noesis.register("EA PSH (PS1) FILES", ".psh")
    noesis.setHandlerTypeCheck(handle, ea_image_check_type)
    noesis.setHandlerLoadRGBA(handle, ea_image_load)

    if debug_mode_enabled:
        noesis.logPopup()
    return 1


def ea_image_check_type(file_data):
    bs = NoeBitStream(file_data)
    signature = bs.readBytes(4).decode("UTF8")
    if (
            signature != "SHPS"      # SSH (PS2)
            and signature != "SHPX"  # XSH (XBOX))
            and signature != "SHPI"  # FSH (PC)
            and signature != "SHPP"  # PSH (PS1)
            and signature != "SHPM"  # MSH (PSP)
    ):
        return 0
    return 1


def get_uint24(in_bytes, endianess):
    if endianess == "<":
        result = struct.unpack(endianess + "I", in_bytes + b"\x00")[0]
    else:
        result = struct.unpack(endianess + "I", b"\x00" + in_bytes)[0]
    return result


def ea_image_load(ea_image_file_data, tex_list):
    print("EA_GRAPH_MAN script v", SCRIPT_VERSION, " (", SCRIPT_LAST_UPDATE, ")")
    bs = NoeBitStream(ea_image_file_data)
    base_name = rapi.getInputName().split('\\')[-1].split('.')[0]
    print("base_name: ", base_name)

    # header parsing
    signature = bs.readBytes(4).decode("UTF8")  # e.g. "SHPS"
    total_file_size = bs.readUInt()
    number_of_entries = bs.readUInt()
    directory_id = bs.readBytes(4).decode("UTF8")  # e.g. "G354", "G264" etc.

    # directory parsing
    entry_tags_list = []
    entry_offsets_list = []
    for i in range(number_of_entries):
        entry_tags_list.append(bs.readUInt())
        entry_offsets_list.append(bs.readUInt())

    # image data parsing
    for i in range(number_of_entries):
        bs.seek(entry_offsets_list[i], NOESEEK_ABS)  # go to entry offset

        entry_type = bs.readUByte()
        pixel_total_size = get_uint24(bs.readBytes(3), "<")
        print("entry_type: ", entry_type)
        print("pixel_total_size: ", pixel_total_size)

        img_width = bs.readUShort()
        img_height = bs.readUShort()
        bs.seek(8, NOESEEK_REL)  # skip reading XY coordinates




        # here starts reading image data
        if entry_type == 1:
            bits_per_pixel = 4
            pixel_size = img_width * img_height // 2
            pixel_data = bs.readBytes(pixel_size)

            bytes_per_palette_pixel = 4
            palette_type = bs.readUByte()
            print("palette_type:", palette_type)
            palette_total_size = get_uint24(bs.readBytes(3), "<")
            palette_width = bs.readUShort()
            palette_height = bs.readUShort()
            bs.seek(8, NOESEEK_REL)  # skip unknown bytes
            palette_size = palette_width * palette_height * bytes_per_palette_pixel
            palette_data = bs.readBytes(palette_size)

            pixel_data = rapi.imageDecodeRawPal(pixel_data, palette_data, img_width, img_height, bits_per_pixel,
                                                "r8 g8 b8 a8", noesis.DECODEFLAG_PS2SHIFT)

            texture_format = noesis.NOESISTEX_RGBA32
            texture_name = "%s_%d" % (base_name, i)
            tex_list.append(NoeTexture(texture_name, img_width, img_height, pixel_data, texture_format))




        elif entry_type == 2:
            bits_per_pixel = 8
            bytes_per_pixel = 1
            pixel_size = img_width * img_height * bytes_per_pixel
            pixel_data = bs.readBytes(pixel_size)

            bytes_per_palette_pixel = 4
            palette_type = bs.readUByte()
            print("palette_type:", palette_type)
            palette_total_size = get_uint24(bs.readBytes(3), "<")
            palette_width = bs.readUShort()
            palette_height = bs.readUShort()
            bs.seek(8, NOESEEK_REL)  # skip unknown bytes
            palette_size = palette_width * palette_height * bytes_per_palette_pixel
            palette_data = bs.readBytes(palette_size)

            pixel_data = rapi.imageDecodeRawPal(pixel_data, palette_data, img_width, img_height, bits_per_pixel,
                                                "r8 g8 b8 a8", noesis.DECODEFLAG_PS2SHIFT)

            texture_format = noesis.NOESISTEX_RGBA32
            texture_name = "%s_%d" % (base_name, i)
            tex_list.append(NoeTexture(texture_name, img_width, img_height, pixel_data, texture_format))
            # entry type 2 END




        elif entry_type == 4:
            bytes_per_pixel = 3
            pixel_size = img_width * img_height * bytes_per_pixel
            pixel_data = bs.readBytes(pixel_size)
            pixel_data = rapi.imageDecodeRaw(pixel_data, img_width, img_height, "r8 g8 b8")

            texture_format = noesis.NOESISTEX_RGBA32
            texture_name = "%s_%d" % (base_name, i)
            tex_list.append(NoeTexture(texture_name, img_width, img_height, pixel_data, texture_format))
            # entry type 4 END





        elif entry_type == 5:
            bytes_per_pixel = 4
            pixel_size = img_width * img_height * bytes_per_pixel
            pixel_data = bs.readBytes(pixel_size)

            texture_format = noesis.NOESISTEX_RGBA32
            texture_name = "%s_%d" % (base_name, i)
            tex_list.append(NoeTexture(texture_name, img_width, img_height, pixel_data, texture_format))
            # entry type 5 END







        else:
            message = "Entry type " + str(entry_type) + " is not supported!"
            noesis.messagePrompt(message)
            return 0


    print("\n")
    return 1
